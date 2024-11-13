<template>
	<div>
	<!-- <div style="position: absolute;z-index: 1000;top:7%;right: 10%;">{{teachInfo}}</div>
	<div style="position: absolute;z-index: 1000;top:10%;right: 10%;">{{teachStru}}</div>
	<div style="position: absolute;z-index: 1000;top:13%;right: 10%;">{{prompt}}</div> -->
	<!-- <div style="position: absolute;z-index: 1000;top:16%;right: 10%;">{{output}}</div> -->
<!-- 	<div style="position: absolute;z-index: 1000;top:16%;right: 10%;">{{etherpad_name}}</div> -->
	<el-button icon="el-icon-coin"  @click="saveedu()" style="position: absolute;z-index: 1000;top:7%;right: 2%;">保存</el-button>
	<el-button icon="el-icon-share"  @click="dialogFormVisible = true" style="position: absolute;z-index: 1000;top:10%;right:2%;">分享</el-button>
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
				lessonName:'',
				states:[
				    {
						name:'自定义教学',
						intro:'',
						proce:[]
					},
					{
						name:'探究式教学',
						intro:'探究式教学以问题解决为中心的，注重学生的独立活动，注重体验式教学，着眼于学生的思维能力的培养。',
						proce:['一、情境创设，课程导入','二、分析问题，明确目标','三、动手实践，探究新知','四、课堂总结，建构概念','五、知识巩固，迁移应用'],
					},{
						name:'讲授式教学',
						intro:'该模式以传授系统知识、培养基本技能为目标。其着眼点在于充分挖掘人的记忆力、推理能力与间接经验在掌握知识方面的作用，使学生比较快速有效地掌握更多的信息量。',
						proce:['一、导入新课','二、检查复习','三、讲授新课','四、巩固新课','五、课堂总结','六、布置作业']
					},{
						name:'协作式教学',
						intro:'协作式教学模式是一种强调学生互相合作、参与和共同构建知识的教学方法。它强调学生在教学过程中的积极参与和合作，促进他们的自主学习和批判性思维能力的培养。',
						proce:['一、课程导入，明确主题','二、围绕主题，明确问题','三、小组协作，解决问题','四、成果展示，交流汇报','五、总结评价，优化方案']
					},{
						name:'讲座式教学',
						intro:'对于相对独立或者前沿的教学内容，通过讲座的形式，教师或学生做主题发言，然后集体讨论探讨，让学生通过自学解决自己所能解决的问题，而把教师的主要精力用于指导学生的学习方法，解决教学中的重点、难点，既能加深对学习主题的理解，又扩充了学生学习的知识领域。',
						proce:['一、教师分组，确定讲座主题','二、小组分工，协作准备','三、举行专题讲座','四、提问答疑','五、提交讲稿、报告']
					},{
						name:'情景式教学',
						intro:'应用情境教学法，设置与教学内容相关的情境，将教学内容理论知识和实践技能结合起来，模拟真实场景，通过学生间相互合作和协调，使学生真正成为课堂教学中的主体和自我发展的主体，从而科学有效地解决综合性实验教学中的问题，为理论教学和实践教学的结合提供良好的平台。',
						proce:['一、设置问题情境，确立实验项目','二、小组分配','三、查找资料','四、设计实验方案','五、体验模拟','六、教师点评','七、提交体验报告']
					},{
						name:'研究式教学',
						intro:'在教学的过程中，教师把研究的项目及方向和教学课程相结合，在教师的指导下，通过阅读文献或课题研究，在学习中研究、在研究中学习，遇到了问题深入分析研究，用已有知识学习求解问题所需要的知识，使学习和研究成为一个互动的过程。在研讨中积累知识、培养能力和锻炼思维。',
						proce:['一、教师提出课题','二、小组分工，协作准备','三、深入研究','四、集体研讨','五、完成报告','六、评价']
					},{
						name:'语文阅读课教学',
						intro:'语文阅读课教学模式旨在通过创设情境、课文品读、拓展阅读、知识应用和评价反馈等环节，培养学生的阅读能力、理解能力和写作能力。通过引发学生的兴趣，帮助他们深入理解课文内容，扩展知识面并将所学知识应用到写作中，该教学模式能够全面发展学生的语文素养。',
						proce:['一、创设情境，激发兴趣','二、课文品读，感受新知','三、拓展阅读，知识延伸','四、知识应用，写作训练','五、评价反馈，修正完善']
					},
					{
						name:'古诗阅读教学模式',
						intro:'该模式注重学生对古诗的感知和体验，通过扩展阅读和对照比较，学生能够进一步拓展对古诗的感知和体验，从而更好地欣赏和理解古诗的美。',
						proce:['一、熟知诗人，明晓题意','二、理解诗意，体会诗情','三、扩展阅读，知识迁移','四、对照比较，知识总结']
					}
				],
				teachmode:[],//教学模式
				tab:0,
				
				
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
				this.teachInfo=JSON.parse(sessionStorage.getItem('teachInfo'));
				this.lessonName=this.teachInfo[this.teachInfo.length-1];
				this.teachStru=JSON.parse(sessionStorage.getItem('teachStru'));
				
				let tab=sessionStorage.getItem('tab');
					
					if(tab=='1'){
						
						this.teachmode=[...this.$route.params.freemode];
						this.states[parseInt(tab)-1].proce=[...this.teachmode];
					}else{
						this.tab=parseInt(tab)-1;
						this.teachmode=[...this.states[this.tab].proce];
						
					}
					console.log(this.states[parseInt(tab)-1]);
				this.output=`<h1>${this.lessonName}</h1><br>`;
			},
			//lessonGemStream 流式生成教案
			lessonGemStream(){
				
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
				const sys = `你是一个专业且知识渊博的教师。现在根据提供的教学信息，为我设计一份优质的教案。
				课程信息：${this.teachInfo}
				教学结构：${this.teachStru}
				教学模式：${this.states[this.tab].name}
				`;
				
				let us = `请你运用你的专业知识，输出 ${this.teachStru[i]},输出格式为：
				<h3>${this.teachStru[i]}</h3><p>${this.teachStru[i]}的内容</p>`;
				if(this.obj!=''){
					us=us+'<br>'+this.obj;
					console.log(us);
				}
				if(this.teachStru[i]=="教学过程"){
					us = `教学环节:${this.teachmode}
				请注意，你要遵循我以下要求：
				1-教学过程要与教学环节相对应;
				2-要求教师的行为要具体到具体做法以及知识点详细讲解。
				经过您深思熟虑的思考之后，结合这篇${this.teachInfo[this.teachInfo.length-1]}的内容，并且运用你的专业知识以及以上教学信息，一步一步思考，设计详细的 ${this.teachStru[i]},输出格式为html。
				<h3>${this.teachStru[i]}</h3><p>教学环节一：教师：xxx；学生：xxx；设计意图：xxx；教师：xxx；学生：xxx；设计意图：xxx；教学环节二：xxx</p>`;
				}
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
						temperature: 0,
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
					console.log("output_str"+output_str);
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