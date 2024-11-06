<template>
	<div>
	<!-- <div style="position: absolute;z-index: 1000;top:7%;right: 10%;">{{teachInfo}}</div>
	<div style="position: absolute;z-index: 1000;top:10%;right: 10%;">{{teachStru}}</div>
	<div style="position: absolute;z-index: 1000;top:13%;right: 10%;">{{prompt}}</div> -->
	<!-- <div style="position: absolute;z-index: 1000;top:16%;right: 10%;">{{output}}</div> -->
<!-- 	<div style="position: absolute;z-index: 1000;top:16%;right: 10%;">{{etherpad_name}}</div> -->
	<el-button icon="el-icon-coin"  @click="saveedu()" style="position: absolute;z-index: 1000;top:7%;right: 2%;">保存</el-button>
	<el-button icon="el-icon-share"  @click="dialogFormVisible = true" style="position: absolute;z-index: 1000;top:7%;right: 4%;">分享</el-button>
	<el-dialog title="教案分享" :visible.sync="dialogFormVisible" width="30%" >
	  <el-form :model="form">
	    <el-form-item label="添加用户ID" :label-width="formLabelWidth">
	      <el-input v-model="form.name" autocomplete="off"></el-input>
	    </el-form-item>
	    <el-form-item label="用户权限:" :label-width="formLabelWidth">
	      <el-select v-model="form.limits" placeholder="请选择用户权限">
	        <el-option label="查看" value="view"></el-option>
	        <!-- <el-option label="评论" value="comment"></el-option> -->
			<el-option label="编辑" value="edit"></el-option>
	      </el-select>
	    </el-form-item>
	  </el-form>
	  <div slot="footer" class="dialog-footer">
	    <el-button @click="dialogFormVisible = false">取 消</el-button>
	    <el-button type="primary" @click="dialogFormVisible = false, sharelesson()">确 定</el-button>
	  </div>
	</el-dialog>
	 <iframe name="embed_readwrite" :src='src' id="Lessoncontent"></iframe>
	 
	</div>
</template>

<script>
	import {Insertlesson,getetherpad,setetherpad,createtherpad,getLessondatas,setetherpadHtml,insertshare} from '../api/api.js'
	export default {
		data() {
			return {
				//分享相关变量
				dialogFormVisible: false,
				dialogdownload: false,
				form: {
				  name: '',
				  limits: '',
				},
				formLabelWidth: '120px',
				tableData: [],
				src:'',
				apiKey:'850315921b51572d1b15eab03e5ff5fae31cc336b5d2098df1bdc609648e9e16',
				teachInfo:[],
				teachStru:[],
				prompt:'',
				outputList:[],
				output:'',
				etherpad_name:'',
				lessonName:''
				
				
			}
		},
		mounted() {
			this.getLessonInfo();//得到教案信息
			this.lessonGemStream();
			getLessondatas().then(response =>{
				const id = response.data.length;
				
				//console.log(id);
				var userName=sessionStorage.getItem('user_name');
				var etherpad_name = sessionStorage.getItem('user_name') + id;
				this.etherpad_name= this.teachInfo[this.teachInfo.length-1];
				//console.log(etherpad_name);
				createtherpad(this.apiKey,this.etherpad_name).then(response =>{
					setetherpad(this.apiKey,this.etherpad_name,'').then(response=>{
					    
						var src = 'http://127.0.0.1:9001/p/'+ this.etherpad_name +`?`+`teachInfo=${this.teachInfo}`;
						this.src=src;
						//console.log(src)
					}).catch(error=>{
						console.error('Error:', error);
					}
					)
				})
				.catch(error => {
					console.error('Error:', error);
				});
			
			})
			.catch(error => {
				console.error('Error:', error);
			});
		},
		created() {
			
		},
		methods: {
			//教案分部生成
			
			//获取从inputInfo.vue 中路由过来的值
			getLessonInfo(){
				this.teachInfo=this.$route.params.teachInfo;
				this.lessonName=this.teachInfo[this.teachInfo.length-1];
				this.teachStru=this.$route.params.teachStru;
				this.output=`<h1>${this.lessonName}</h1><br>`;
			},
			//lessonGemStream 流式生成教案
			lessonGemStream(){
				// 整体生成
				this.prompt=`你是一个资深且专业的教学设计机器人。请你根据我提供的教学信息，设计一份优质的教案。
				课程信息：${this.teachInfo}
                授课模式：练习课
                教学结构：${this.teachStru}
                教学模式：探究式教学
				输出格式：html`;
				//console.log(prompt);
				const len=this.teachStru.length;
				this.main(len);
				
			},
			async main(l) {
				//分部生成
			  for (let i = 0; i < l; i++) {
			    await this.generateTextStream(i);
			  }
			},
			async generateTextStream(i) {
				const sys = `你是一个资深且专业的教学设计机器人。请你根据我提供的教学信息，设计一份优质教案。
				课程信息：${this.teachInfo}
				授课模式：练习课
				教学结构：${this.teachStru}
				教学模式：探究式教学
				`;
				const us = `请你运用你的专业知识，输出 ${this.teachStru[i]},输出格式为：
				<h3>${this.teachStru[i]}</h3><div>${this.teachStru[i]}的内容<div>`;
				const API_KEY = 'cfcea42fdab447bd8907728beaa56417';
				let output = '';
				let output_str = '';
				const url =
					"https://team3-at-2.openai.azure.com/openai/deployments/GPT35/chat/completions?api-version=2023-03-15-preview";
				//直接获取 Fetch 的response， 无法使用 await的话， Promise的方式也是可以的。
				const response = await fetch(url, {
					method: "POST",
					body: JSON.stringify({
						max_tokens: 3000,
						n: 1,
						temperature: 0.5,
						frequency_penalty: 0,
						presence_penalty: 0,
						top_p: 0.95,
						stop: null,
						stream: true,
						// model:MODEL,
						messages: [{
								role: 'system',
								content: sys
							},
							{
								role: 'user',
								content: us
							}
						]
					}),
					headers: {
						'api-key': API_KEY,
						'Content-Type': 'application/json',
					}
				})
				//获取UTF8的解码
				const encode = new TextDecoder("utf-8");
				//获取body的reader
				const reader = response.body.getReader();
				// 循环读取reponse中的内容
				while (true) {
			
					const {
						done,
						value
					} = await reader.read();
					if (done) {
						break;
					}
					// 解码内容
					//开始处理解码后的内容
					//data: {"id":"chatcmpl-88NzPq1B3YvhsdYbA3kAFz1HKh2vu",
					// "object":"chat.completion.chunk",
					// "created":1697009531,
					// "model":"gpt-35-turbo",
					// "choices":[{"index":0,"finish_reason":null,"delta":{"role":"assistant"}}],"usage":null}
					const text = encode.decode(value);
					//第一步：处理成列表数组，去掉数组第一和(最后一轮生成的内容)最后一个
					let data1 = text.split("data:");
					//console.log(data1)
					let data2 = data1.slice(1)
					//slicez作用主要是剪掉数组第一个值为''
					//console.log(data2)
					for (var i = 0, len = data2.length; i < len; i++) {
						console.log(data2[i]);
						data2[i] = data2[i].replace("\n\n", "");
						if (!data2[i].includes('[DONE]')) {
							//当JSON.parse data2[i]不符合json格式时会中断
							if(data2[i]){
								let parsedData = JSON.parse(data2[i]);
								if (parsedData['choices'][0]['delta']) {
									// 当获取错误token时，输出错误信息
									if (text === "<ERR>") {
										output = "Error";
										break;
									} else {
										// 获取正常信息时，逐字追加输出 
										if(parsedData['choices'][0]['delta']['content']){
											output_str +=parsedData['choices'][0]['delta']['content'];
										}
										
									}
								}
							}
							
							
						}
					}
					//数据库连接
					
			
					this.outputList.push(output_str);
					// this.output += output_str.replace(/\n/g, "<br>", ); //对于ai生成的东西进行处理，由于字符串中的/n表示换行+空一行，而<br>可以只换行
					this.output += output_str.replace("<br>", "",);
					//this.output += output_str;
					output_str = '';
					
					
					setetherpadHtml(this.apiKey,this.etherpad_name,this.output).then(response=>{
						//console.log(response.data)
					}).catch(error=>{
						console.error('Error:', error);
					}
					)
					
					// console.log(this.output);
				}
				// this.insertNewNode();
				const result=i;
				return result;
			
			},
			
			
			
			//保存教案到数据库中
			saveedu() {
				sessionStorage
				//const user_name = 'mqz1';
		
				const user_name = sessionStorage.getItem('user_name');
				var LessonName = this.lessonName;
				var Navigation = 'mqz1';
				var Lessoncontent = document.getElementById("Lessoncontent").outerHTML;
				
			
				Insertlesson(user_name, LessonName, Navigation, Lessoncontent).then(response => {
			
					if(response.data.status == true){
						// 注册成功，显示成功框 --
						this.$message({
								message: '保存成功',
								type: 'success',
								
								});
						this.$router.push('/Workspace');
						
						
					}
					else
					{
						this.$message.error('保存失败！');
					}
					})
					.catch(error => {
						this.$message.error('保存失败！！');
						});
				
				},
				//分享教案
				sharelesson(){
					const Author = sessionStorage.getItem('user_name');
					const Sharer = this.form.name;
					const Privilege = this.form.limits;
					const Lessonid = this.$route.params.id;
					insertshare(Author,Sharer,Privilege,Lessonid).then(response => {
						if(response.data.status == true){
							// 注册成功，显示成功框
							this.$message({
									message: '分享成功',
									type: 'success'
									});
						}
						else
						{
							this.$message.error(response.data.data);
						}
						})
						.catch(error => {
							this.$message.error('分享失败！！');
							});
				
				},

		}
	}
</script>

<style>
	iframe {
	    display: block;
	    position: absolute;
	    top: 0;
	    left: 0;
	    width: 100%;
	    height: 100%;
	    border: none;
	  }
</style>