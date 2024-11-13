<template>
	<div>
		<el-row style="width: 100%; padding: 0.75rem 0; display: flex; justify-content: space-between; align-items: center;">
		    <el-col :span="8" style="text-align: left;margin-left: 1.875rem;">  
		      <p><el-button type="primary">实验条件3：智能教案生成</el-button></p>  
			  <p><el-tag type="warning">教案任务详细介绍请点击最右侧蓝色图标</el-tag></p>
		    </el-col>  
			<el-col :span="8" style="text-align: center;">  
			<el-button>经历时间：{{ elapsedTime }}</el-button>
			</el-col>
		    <el-col :span="8" style="text-align: right;margin-right: 0.875rem;">  
		      <el-button icon="el-icon-coin" @click="saveedu()">完成</el-button>  
		      <el-button icon="el-icon-user" circle></el-button>  
		    </el-col>  
		  </el-row>
		

		<el-row type="flex" class="row-bg" justify="space-between">
			<el-col class="col01" :sm="1" :md="3" :lg="3" :xl="3">
			  <!-- <el-button @click="lessonGemStreamButton">重新生成教案</el-button> -->
			</el-col>
			<el-col :sm="23" :md="24" :lg="23" :xl="23">
				<div class="box" ref="box">
					<div class="left">
						<!--左侧div内容-->
						<div>
							<!-- 工具栏 -->
							<Toolbar :editor="editor" :defaultConfig="toolbarConfig" />
							<!-- 编辑器 -->
							<Editor id="content" :style="editorChange" :defaultConfig="editorConfig"
								v-model="html" @onChange="onChange" @onCreated="onCreated" v-katex:auto />
							<div style="width: 180px;  position: absolute;left: 0;top: 30%;"  >
								<ul id="header-container" ></ul>
							</div>
							 


						</div>
					</div>
					<div class="resize" title="收缩侧边栏" v-show="PromptStoreVisual">
						⋮
					</div>
					<!-- AI提示词模板显示区域 -->
					<div class="mid" v-show="PromptStoreVisual">
							<el-header><el-button type="primary" round size="small"
									class="title">任务步骤</el-button></el-header>
								<el-scrollbar wrap-class="message-list" wrap-style="margin-top:20px;padding-left:20px;">
									<div v-for="(item,index) in options4" :key="index" style="margin-top: 10px;">
										<p class="prom"> {{ item }}</p>
									</div>
								</el-scrollbar>
							<el-header><el-button type="primary" round size="small"
									class="title">教学模式</el-button></el-header>
							<el-select v-model="selectedState" placeholder="请选择教学模式">  
							      <el-option  
							        v-for="state in states"  
							        :key="state.name"  
							        :label="state.name"  
							        :value="state.name">  
							      </el-option>  
							 </el-select> 
							 <!-- 显示选中模式的详细介绍和过程 -->  
							    <div v-if="selectedState" style="margin: 0.5rem 1.2rem;" class="prom">   
							      <p>{{ getIntroByName(selectedState) }}</p>
								  <p>教学环节：</p>
							        <p v-for="(step, index) in getProceByName(selectedState)" :key="index">{{ step }}</p>    
							    </div>  	
					</div>

				</div>
			</el-col>
			<el-col :sm="1" :md="1" :lg="1" :xl="1" class="bg-right">
				<el-row>
					<div class="buttonAI" @click="clickBtnStore"><el-avatar :size="40" :src="img_Store"></el-avatar>
					</div>
				</el-row>

			</el-col>
		</el-row>
		<!-- start 点击完成实验之后，弹出这个框框 -->
		<el-dialog title="完成信息" :visible.sync="dialogForm4Visible">
			<p>您完成教案所耗费的时间为：{{timeGo}},总的教案字数为：{{lessonSum}}</p>
			<p>接下来，请填写一份针对于该实验条件下的调查问卷。</p>
		    <p>填写网址：<a href="https://www.wjx.cn/vm/OPGQFi9.aspx" target="_blank">实验条件3 调查问卷</a> <p>
			<p>填写完毕后，请点击回到实验任务首页:</p>
			<el-button @click="backToSum">实验任务首页</el-button>
		  
		</el-dialog>
		<!-- end -->
	</div>
</template>

<script>
import {insertstudyorder,insertstudyorderc,insertstudtime,inserthistoryc,inserthistoryaia,getstudyorder,getstudyorderc} from '../api/api.js'
	import imgAI from '@/assets/AI助手@2x.svg'
	import imgMY from '@/assets/人.svg'
	import imgStore from '@/assets/库存.svg'
	//引入wangEditor编辑器
	import {
		Editor,
		Toolbar
	} from "@wangeditor/editor-for-vue";
	import {
		DomEditor,
		SlateTransforms,
		SlateEditor,
		SlateElement,
		SlateNode
	} from '@wangeditor/editor'
	import {
		Boot,
		IModuleConf
	} from '@wangeditor/editor'
	
	import MyButtonMenu from '../js/new_file.js'
	
	//引入mapState映射，用来获得store数据
	import {
		mapState
	} from 'vuex'
	import {
		Card,
		Header
	} from 'element-ui';
	import {
		vnode
	} from 'snabbdom';
	
	export default {
		name: "MyEditor",
		components: {
			Editor,
			Toolbar,
		},
		computed: {
			//mapState默认会把state当第一个参数传进来
			...mapState({
				LesInfo: state => state.Lesson.LesInfo, //获得ai生成教案的基本信息。
				Les: state => state.Lesson.Les //教案生成的内容
			})

		},
		data() {
			return {
				//得到studySum的匹配过来的教案主题
				matchT:'',
				/*测试ai生成教案功能*/
				headerContainer: '',
				outputList: [],
				input:'',//存储语音文本
				output: '', //ai生成的教案内容
				output1: '', //ai生成的教案内容
				outcome: '', //ai修改的语句
				come: '',
				/*ai助手相关变量*/
				AIVisual: false, //ai助手聊天框点击交互v-show参数
				VoiceClick: false, //语音功能点击交互参数
				PromptStoreVisual: false,
				voice: '', //voice未实例化
				selectStr: '',
				inputMessage: '',
				tip: '请输入内容',
				tipAdress: {},
				img_AI: imgAI,
				img_MY: imgMY,
				img_Store: imgStore,
				messages: [{
						sender: 'AI',
						content: ['', '您好呀，我是教案AI助手。您想生成的教案的基本信息为：<br>一年级 小学 语文 《识字-金木水火土》 ']
					},
					{
						sender: 'MY',
						content: '你好呀'
					},
					// {
					// 	sender: 'AI',
					// 	content: ['你好呀','siri']
					// }
				],
				/*wangEditor相关变量*/
				editor: null,
				html: "",
				toolbarConfig: {
					//toolbarKeys: [ 'MyButtonMenu' ],
					excludeKeys: ['blockquote', 'group-more-style', 'insertLink', 'group-video', 'fullScreen'],
				},
				editorConfig: {
					placeholder: "这里显示教案内容...",
					// autoFocus: false,

					scroll: true,
					hoverbarKeys: {
						'text': {
							menuKeys: ['headerSelect', 'bold', 'underline', 'italic', '|', 'fontSize',
								'fontFamily',
							], // 定义你想要的 menu keys'MyButtonMenu',
						}
					},

					// 所有的菜单配置，都要在 MENU_CONF 属性下
					MENU_CONF: {},
				},
				// 任务详细
				options4: [],
				// 教学模式
				options3: [],
				value9: [],
				list: ['AA'],
				loading: false,
				// 选中的教学模式名称  
				selectedState: '',
				states:[
				{
						name:'',
						intro:'',
						proce:[],
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
					},
					{
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
				 //定时器
				 startTime: null, // 计时开始时间  
				 timerId: null, // 定时器ID   
				 elapsedTime: '00:00:00', // 已运行时间
				 timeGo:'00:00:00',
				 isTimerRunning:false,
				 editorChange:{
				  height:'85vh',
				  overflowY: 'auto',
				 },
				 //总字数
				 lessonSum:0,
				 teachInfo:[],
				 teachStru:[],
				 dialogForm4Visible:false,
				 order:'',//获取当前实验的实验顺序
				 user_name:'',
				 radio:'',
				 teachmode:[],//教学模式
				 tab:0,
				 obj:'',//教学目标




			}
		},
		watch: {
			output() {

				//改变策略
				this.html = `<p>${this.output}</p>`;

			},
			input(){
				this.inputMessage=`${this.input}`;
			},
	
			outcome() {
				this.come = this.outcome;
			},
		},
		mounted() {
			this.user_name = sessionStorage.getItem('user_name');
		    console.log('我在这里：'+this.user_name);
			//获取对应的教案信息
			this.getLessonInfo();
			this.lessonGemStream();
			////获取实验对应的教案主题
			this.getLessonPlanName();
			// 开始计时   
			this.startTimer();
			

			//寻找header标签并且得到对应的id成为大纲
			this.headerContainer = document.getElementById('header-container')
			    this.headerContainer.addEventListener('mousedown', event => {
			      if (event.target.tagName !== 'LI') return
			      event.preventDefault()
			      var id = event.target.id
				  console.log(id);
			      this.editor.scrollToElem(id) // 滚动到标题
			    })
			this.clickBtnStore();
			this.dragControllerDiv();
			

		},
		created() {

		},

		methods: {
			backToSum(){
				this.$router.push('/studySum');
				console.log('click me');
			},
			// 根据选中的教学模式名称获取介绍  
			getIntroByName(name) {  
			      const state = this.states.find(s => s.name === name);  
			      return state ? state.intro : '未找到介绍';  
			    },  
			    // 根据选中的教学模式名称获取过程步骤  
			    getProceByName(name) {  
			      const state = this.states.find(s => s.name === name);  
			      return state ? state.proce : [];  
			    }, 
			//获取从inputInfo.vue 中路由过来的值
			getLessonInfo(){
				 //teachInfo teachStru startTime tab freemode
			// 	 sessionStorage.setItem('teachInfo', JSON.stringify(t));
            //    sessionStorage.setItem('teachStru', JSON.stringify(cv));
			//    sessionStorage.setItem('startTime',st);
			//    sessionStorage.setItem('tab',tab);
            //    sessionStorage.setItem('freemode', JSON.stringify(freeMode));
			this.teachInfo=JSON.parse(sessionStorage.getItem('teachInfo'));
			this.lessonName=this.teachInfo[this.teachInfo.length-1];
			this.teachStru=JSON.parse(sessionStorage.getItem('teachStru'));
			this.order=parseInt(sessionStorage.getItem('index'))+1;
			this.radio=sessionStorage.getItem('radio');
			let tab=sessionStorage.getItem('tab');




				// this.teachInfo=this.$route.params.teachInfo;
				// this.lessonName=this.teachInfo[this.teachInfo.length-1];
				// this.teachStru=this.$route.params.teachStru;
				// this.order=this.$route.params.order;
				// this.radio=this.$route.params.radio;
				// console.log('radio传:'+this.radio);
				// //tab:tab,freemode:freeMode,
				// let tab=this.$route.params.tab;
				// console.log('tab:'+tab);
				if(tab=='1'){
					console.log('tab 1 freeMode传:'+this.$route.params.freemode);
					this.teachmode=[...this.$route.params.freemode];
					this.states[parseInt(tab)-1].proce=[...this.teachmode];
					console.log('tab 1 this.teachmode:'+this.teachmode)
					console.log('tab 1 this.states[parseInt(tab)-1].proce:'+this.states[parseInt(tab)-1].proce);
				}else{
					this.tab=parseInt(tab)-1;
					this.teachmode=[...this.states[this.tab].proce];
					console.log('tab this.teachmode:'+this.teachmode)
				}

				console.log('me'+this.order);
				this.output=`<h1>${this.lessonName}</h1><br>`;
				
			},
			//lessonGemStream 流式生成教案
			lessonGemStream(){
				// 整体生成
				
				//console.log(prompt);
				const len=this.teachStru.length;
				this.main(len);
				
			},
			//获取实验对应的教案主题
			getLessonPlanName(){
				this.matchT=this.$route.params.matchTheme;
				this.startTime = this.$route.params.startTime;  
				this.options4=[`1-您在此实验中被分配的教案任务为:${this.matchT}`,'2-在此实验中，希望您能优化这份生成的教案，除了我们提供的参考资料，请不要访问其他资料网站工具。',
			'3-点击完成实验 按钮之后，结束此次教案设计。'];
				console.log(this.$route.params.matchTheme);
			},
			// 开始计时
			    startTimer() {  
			      if (!this.isTimerRunning) {  
			        // this.startTime = this.$route.params.startTime;  
			        this.timerId = setInterval(() => {  
			          this.updateElapsedTime();  
			        }, 1000); // 每秒更新一次时间  
			        this.isTimerRunning = true;  
			      }  
			    },  
			    // 更新已运行时间  
			    updateElapsedTime() {  
			      const now = new Date();  
			      const diff = now - this.startTime;  
			      const hours = Math.floor(diff / (1000 * 60 * 60));  
			      const minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));  
			      const seconds = Math.floor((diff % (1000 * 60)) / 1000);  
			  
			      this.elapsedTime = `${String(hours).padStart(2, '0')}:${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`;  
			    },
				saveedu(){
					if(this.timeGo=='00:00:00'){
						this.timeGo=this.elapsedTime;
					}
					this.dialogForm4Visible = true;
					
					//完成实验之后，把数据库中对应的实验orderc设置为1
					//1-确定当前实验是该用户的第几个实验this.order
					//2-把数据库中的对应的顺序设为1，表明已经完成该实验；
				insertstudyorderc(this.user_name,`${this.order}`).then(response =>{
					this.$message({
						message: '成功！',
						type: 'success'
						});
				})
				.catch(error => {
					console.error('Error:', error);
				}); 
				// 3-完成实验需要记录实验数据
				insertstudtime('实验3',this.user_name,this.radio,this.timeGo,this.lessonSum,this.html).then(response =>{
					this.$message({
						message: '成功！',
						type: 'success'
						});
				})
				.catch(error => {
					console.error('Error:', error);
				});
				},
			//box拖拽条改变宽度
			dragControllerDiv: function() {
				var resize = document.getElementsByClassName('resize');
				var left = document.getElementsByClassName('left');
				var mid = document.getElementsByClassName('mid');
				var box = document.getElementsByClassName('box');
				var col01 = document.getElementsByClassName('col01');
				// 鼠标按下事件
				resize[0].onmousedown = function(e) {
					//颜色改变提醒
					resize[0].style.background = '#818181';
					var startX = e.clientX - col01[0].offsetWidth;
					resize[0].left = resize[0].offsetLeft;
					// 鼠标拖动事件
					document.onmousemove = function(e) {
						var endX = e.clientX - col01[0].offsetWidth;
						var moveLen = resize[0].left + (endX - startX) - col01[0]
							.offsetWidth; // （endx-startx）=移动的距离。resize[i].left+移动的距离=左边区域最后的宽度
						var maxT = box[0].clientWidth - resize[0].offsetWidth; // 容器宽度 - 左边区域的宽度 = 右边区域的宽度

						if (moveLen < 32) moveLen = 32; // 左边区域的最小宽度为32px
						if (moveLen > maxT - 150) moveLen = maxT - 150; //右边区域最小宽度为150px

						resize[0].style.left = moveLen; // 设置左侧区域的宽度

						left[0].style.width = moveLen + 'px';
						mid[0].style.width = (box[0].clientWidth - moveLen - 10) + 'px';
					};
					// 鼠标松开事件
					document.onmouseup = function(evt) {
						//颜色恢复
						resize[0].style.background = '#d6d6d6';
						document.onmousemove = null;
						document.onmouseup = null;
						resize[0].releasePointerCapture && resize[0].releasePointerCapture(1);
						//当你不在需要继续获得鼠标消息就要应该调用ReleaseCapture()释放掉
					};
					resize[0].setPointerCapture && resize[0].setPointerCapture(1); //该函数在属于当前线程的指定窗口里设置鼠标捕获
					return false;
				};
			},
			//ai助手发送信息
			sendMessage() {

				// this.insertNewNode();
				this.outcome = '';
				//const voiceTxt = document.querySelector('#voiceTxt'); //采用dom方式可操作教师输入框，否则，当text改变时，教师输入框可不会自动更新
				//console.log("send:"+voiceTxt.value);
				//this.inputMessage=voiceTxt.value;
				if (this.inputMessage.trim()) {
					this.messages.push({
						sender: 'MY',
						content: this.inputMessage
					})
					this.generateTextStreamToParagraph(); //异步了。	
					// this.inputMessage = '';


				}

			},
			//ai助手更新消息
			updateMessage() {

				// this.insertNewNode();
				this.outcome = '';
				this.generateTextStreamToParagraph(); //异步了。	




			},
			//点击buttonAI把mid宽度修改为0%，left宽度为100%
			clickBtnAI() {
				// console.log("触发了clickbtnai");
				var resize = document.getElementsByClassName('resize');
				var left = document.getElementsByClassName('left');
				var mid = document.getElementsByClassName('mid');
				if (!this.AIVisual) {
					this.AIVisual = true;
					// console.log(this.AIVisual);
					left[0].style.width = 68 + '%';
					mid[0].style.width = 'calc(' + 32 + '% - ' + 10 + 'px)';
				} else {
					this.AIVisual = false;
					// console.log(this.AIVisual);
					mid[0].style.width = 0 + '%';
					left[0].style.width = 100 + "%";
				}

			},
			//点击buttonAI把mid宽度修改为0%，left宽度为100%
			clickBtnStore() {
				// console.log("触发了PromptStoreVisual");
				var resize = document.getElementsByClassName('resize');
				var left = document.getElementsByClassName('left');
				var mid = document.getElementsByClassName('mid');
				if (!this.PromptStoreVisual) {
					this.PromptStoreVisual = true;
					// console.log(this.PromptStoreVisual);
					left[0].style.width = 68 + '%';
					mid[0].style.width = 'calc(' + 32 + '% - ' + 10 + 'px)';
				} else {
					this.PromptStoreVisual = false;
					// console.log(this.PromptStoreVisual);
					mid[0].style.width = 0 + '%';
					left[0].style.width = 100 + "%";
				}

			},
			//点击语音
			startVoice() {

				if (!this.VoiceClick) {
					console.log("正在听取你的声音中...");
					this.voice.start();
					this.VoiceClick = true;
				} else {
					console.log("正在暂停倾听你的声音中...");
					this.voice.stop();
					this.VoiceClick = false;
				}
			},

			//MyEditor相关事件
			onCreated(editor) {

				this.editor = Object.seal(editor); // 【注意】一定要用 Object.seal() 否则会报错

			},
			//当ai进行生成的时候，插入一个新节点
			insertNewNode(h) {
				var header3Element = {
					type: 'header3',
					children: [{
							text: `${h}`,

					}],
				};
				this.editor.insertNode(header3Element);
				// console.log(this.editor.children)

			},
			selectInsert(changeText) {

				this.editor.select(this.tipAdress)
				this.editor.dangerouslyInsertHtml(changeText);
				// this.editor.dangerouslyInsertHtml('<p style="text-align:left;border:2px solid #ff5500;">hello</p>');
			},
			handleEnter() {
				// console.log('按钮被点击了');
				//editor.insertText('<br>');
			},
			onChange(editor) {


				// const toolbar = DomEditor.getToolbar(editor)
				// const curToolbarConfig = toolbar.getConfig()
				// console.log( curToolbarConfig.toolbarKeys ) // 当前菜单排序和分组
				//如果editor中的内容有选中,就选中当前选中的地方；若未选中，则会显示null，还是显示之前选中的文本内容。

				if (editor.selection != null) {
					this.tipAdress = editor.selection
					//this.selectStr=editor.getSelectionText();
					//editor.addMark('color', '#999') ;//标记选中的文本
				}
				//如果鼠标选中不在editor了，也会记得之前选中的最后一次地方
				editor.select(this.tipAdress);

				// console.log("this.selectStr:" + this.selectStr);

				this.tip = '更改文本' + '" ' + editor.getSelectionText().toString().substring(0, 60) + '"'; //显示输入框提示文本
				// editor.insertText('xxx');出现卡顿错误
				this.selectStr = editor.getSelectionText();
				// console.log('onChange', editor.getHtml()) // onChange 时获取编辑器最新内容
				const headerContainer = document.getElementById('header-container')
				const headers = editor.getElemsByTypePrefix('header')
				headerContainer.innerHTML = headers.map(header => {
					let i=1;
					const text = SlateNode.string(header)
					// console.log(text)
					const {
						id,
						type
					} = header
					 return `<li id="${id}" type="${type}" style='padding: 10px 0px;color: #33081b;cursor: pointer;border: #bfbfbf 1px solid;border-radius: 0.3125rem;font-size:13px;'><i class="el-icon-menu" style="margin-right:5px;"></i>${text}</li>`
				}).join('')
				const text = editor.getText();
				this.lessonSum=text.length;


			},
			getEditorText() {
				const editor = this.editor;
				if (editor == null) return;

				// console.log('getEditorText', editor.getText()); // 执行 editor API
			},
			printEditorHtml() {
				const editor = this.editor;
				if (editor == null) return;

				// console.log(editor.getHtml()); // 执行 editor API
			},
			async main(l) {
				//分部生成
			  for (let i = 0; i < l; i++) {
			    await this.generateTextStream(i);
			  }
			},
			lessonGemStreamButton(){
				
				this.lessonGemStream();
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
				2-要求教学环节包含老师的知识点讲解、学生的具体反应、教师与学生的互动过程。
				经过您深思熟虑的思考之后，并且运用你的专业知识以及以上教学信息，设计详细的 ${this.teachStru[i]},输出格式为html。
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
						//console.log(data2[i]);
						data2[i] = data2[i].replace("\n\n", "");
						if (!data2[i].includes('[DONE]')) {
							//当JSON.parse data2[i]不符合json格式时会中断
							if(data2[i]){
								let parsedData = JSON.parse(data2[i]);
	// 							let parsedData = '';
	// 							try {
    //   parsedData = JSON.parse(data2[i]);
    //   // 这里进行后续处理
    //   console.log(parsedData);
    // } catch (error) {
    //   // JSON 解析失败，重新点击按钮（这里只是模拟重新点击按钮的行为，实际中你需要根据具体情况触发按钮点击事件）
    //   console.log('JSON 解析失败，重新点击按钮');
    //   break;
    // }
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
					 //this.output += output_str.replace(/\n/g, "<br>", ); //对于ai生成的东西进行处理，由于字符串中的/n表示换行+空一行，而<br>可以只换行
					// this.output += output_str.replace("<br>", "",);
					this.output += output_str.replace("<br>", "",);
					//this.output += output_str;
					output_str = '';
					if(i==0){//教学目标
						this.obj=this.output;
					}
					
					// setetherpadHtml(this.apiKey,this.etherpad_name,this.output).then(response=>{
					// 	//console.log(response.data)
					// }).catch(error=>{
					// 	console.error('Error:', error);
					// }
					// )
					
					// console.log(this.output);
				}
				// this.insertNewNode();
				const result=i;
				return result;
			
			},
			// //ai流式生成教案
			// async generateTextStream() {
				
			// 	const sys = `你是教学设计机器人，我将提供教学信息给你，你的工作是为老师生成一份完整的教案.`;
			// 	const us = `教学信息在以下三个反引号（\`\`\`）内：\n\`\`\`\n 识字-金木水火土 一年级 小学 语文\n\`\`\`\`
			// 	我想要提出要求：每一个教学要素都不少于100字，其中教学过程要求不少于500字。
			// 	要求输出格式为：
			// 	<h3>教学内容分析</h3>
			// 	<p>{教学内容分析的内容}</p>
			// 	<h3>教学目标</h3>
			// 	<h3>学习重难点</h3>
			// 	<h3>学习者分析</h3>
			// 	<h3>教学过程</h3>
				
			// 	请注意，请严格遵守以上输出格式，不要出现其他话语,不要出现空行`;

			// 	const API_KEY = process.env.VUE_APP_API_KEY;
			// 	let output = '';
			// 	let output_str = '';
			// 	const url =
			// 		"https://team3-at-2.openai.azure.com/openai/deployments/GPT35/chat/completions?api-version=2023-03-15-preview";
			// 	//直接获取 Fetch 的response， 无法使用 await的话， Promise的方式也是可以的。
			// 	const response = await fetch(url, {
			// 		method: "POST",
			// 		body: JSON.stringify({
			// 			max_tokens: 3000,
			// 			n: 1,
			// 			temperature: 0.5,
			// 			frequency_penalty: 0,
			// 			presence_penalty: 0,
			// 			top_p: 0.95,
			// 			stop: null,
			// 			stream: true,
			// 			// model:MODEL,
			// 			messages: [{
			// 					role: 'system',
			// 					content: sys
			// 				},
			// 				{
			// 					role: 'user',
			// 					content: us
			// 				}
			// 			]
			// 		}),
			// 		headers: {
			// 			'api-key': API_KEY,
			// 			'Content-Type': 'application/json',
			// 		}
			// 	})
			// 	//获取UTF8的解码
			// 	const encode = new TextDecoder("utf-8");
			// 	//获取body的reader
			// 	const reader = response.body.getReader();
			// 	// 循环读取reponse中的内容
			// 	while (true) {

			// 		const {
			// 			done,
			// 			value
			// 		} = await reader.read();
			// 		if (done) {
			// 			break;
			// 		}
			// 		// 解码内容
			// 		//开始处理解码后的内容
			// 		//data: {"id":"chatcmpl-88NzPq1B3YvhsdYbA3kAFz1HKh2vu",
			// 		// "object":"chat.completion.chunk",
			// 		// "created":1697009531,
			// 		// "model":"gpt-35-turbo",
			// 		// "choices":[{"index":0,"finish_reason":null,"delta":{"role":"assistant"}}],"usage":null}
			// 		const text = encode.decode(value);
			// 		//第一步：处理成列表数组，去掉数组第一和(最后一轮生成的内容)最后一个
			// 		let data1 = text.split("data:");
			// 		//console.log(data1)
			// 		let data2 = data1.slice(1)
			// 		for (var i = 0, len = data2.length; i < len; i++) {
			// 			data2[i] = data2[i].replace("\n\n", "");
			// 			if (!data2[i].includes('[DONE]')) {
			// 				if (JSON.parse(data2[i])['choices'][0]['delta']['content']) {
			// 					// 当获取错误token时，输出错误信息
			// 					if (text === "<ERR>") {
			// 						output = "Error";
			// 						break;
			// 					} else {
			// 						// 获取正常信息时，逐字追加输出 
			// 						output_str += JSON.parse(data2[i])['choices'][0]['delta']['content'];
			// 					}
			// 				}
			// 			}
			// 		}
			// 		//数据库连接
					

			// 		this.outputList.push(output_str);
			// 		// this.output += output_str.replace(/\n/g, "<br>", ); //对于ai生成的东西进行处理，由于字符串中的/n表示换行+空一行，而<br>可以只换行
			// 		this.output += output_str.replace("<br>", "",);
			// 		//this.output += output_str;
			// 		output_str = '';
			// 		// console.log(this.output);
			// 	}
			// 	// this.insertNewNode();

			// },
			//ai逐句修改补充
			async generateTextStreamToParagraph() {

				this.outcome = ''; //将上一次ai获得的答案进行清空
				let selectStr = this.selectStr;
				
				const sys = `你是一个专业的教学设计机器人。我的教案主题是 识字-金木水火土 一年级 小学 语文 。`;
				let us='';
				if(selectStr==''){
					us =`${this.inputMessage}.`;
				}else{
					 us = `我的教案主题是 识字-金木水火土 一年级 小学 语文 。我选中的一段话是${selectStr}.修改要求是${this.inputMessage}.请你根据我提出的需求和教案主题修改我选中的一段话，输出修改的内容即可，无需其他话语。让我们一步一步思考，确保得出正确的结论`;
				}
				

				const API_KEY = process.env.VUE_APP_API_KEY;
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
					const text = encode.decode(value);
					//第一步：处理成列表数组，去掉数组第一和(最后一轮生成的内容)最后一个
					let data1 = text.split("data:");
					//console.log(data1)
					let data2 = data1.slice(1)
					for (var i = 0, len = data2.length; i < len; i++) {
						data2[i] = data2[i].replace("\n\n", "");
						if (!data2[i].includes('[DONE]')) {
							if (JSON.parse(data2[i])['choices'][0]['delta']['content']) {
								// 当获取错误token时，输出错误信息
								if (text === "<ERR>") {
									output = "Error";
									break;
								} else {
									// 获取正常信息时，逐字追加输出 
									output_str += JSON.parse(data2[i])['choices'][0]['delta']['content'];
								}
							}
						}
					}

					this.outputList.push(output_str);
					this.outcome += output_str.replace(/\n/g, ""); //对于ai生成的东西进行处理，由于字符串中的/n表示换行+空一行，而<br>可以只换行
					output_str = '';

				}

				//生成且更新教师要求的信息
				let length = this.messages.length;
				let last = this.messages[length - 1];
				// console.log(last);
				if (last.sender == 'AI') {
					this.messages.pop();
					this.messages.push({
						sender: 'AI',
						content: [this.selectStr, this.outcome],
					})
				} else {
					this.messages.push({
						sender: 'AI',
						content: [this.selectStr, this.outcome]
					})
				}




			},
			//提示词模板相关函数
			remoteMethod(query) {
				if (query !== '') {
					this.loading = true;
					setTimeout(() => {
						this.loading = false;
						this.options4 = this.list.filter(item => {
							return item.label.toLowerCase()
								.indexOf(query.toLowerCase()) > -1;
						});
					}, 200);
				} else {
					this.options4 = [];
				}
			},
			//触发点击大纲函数
			handleOpen(key, keyPath) {
				console.log(key, keyPath);
			},
			handleClose(key, keyPath) {
				console.log(key, keyPath);
			},
			selectNav(index, indexPath) {
				console.log(index, indexPath);
			},
			//html转换为word
			convertToword(){
				const fileName=`${this.LesInfo.lname}.docx`;
				console.log('这里是触发了convertToword函数，word名称为：'+this.LesInfo.lname);
				const fullHtmlContent = `
				    <!DOCTYPE html>
				    <html>
				      <head>
				        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
				      </head>
				      <body>
				        ${this.html}
				      </body>
				    </html>
				  `;
				// 使用 html-docx-js 将 HTML 转换为 Word 文档的 Blob 对象
				const converted = htmlDocx.asBlob(fullHtmlContent);
				// 使用 file-saver 保存 Blob 对象为 Word 文档文件
				FileSaver.saveAs(converted, fileName);	
			},
			changeStyleCom(){
				this.editorChange.height='100%';
				this.editorChange.overflowY='vislble';
			},
			convertToPdf(){
				this.changeStyleCom();
				 // 方法一：htmlToPdf.getPdf(`${this.LesInfo.lname}`); 出现的问题：只能转为当前屏幕上所看到的。
						htmlToPdf.getPdf(`${this.LesInfo.lname}`);
						this.editorChange.height='85vh';
						this.editorChange.overflowY='auto';
						
			},



		},

		beforeDestroy() {
			const editor = this.editor;
			if (editor == null) return;
			editor.destroy(); // 组件销毁时，及时销毁 editor ，重要！！！
		},
	}
</script>

<style scoped>
	/* wangeditor样式 */
	#editor—wrapper {
		height: 100%;
		border: 1px solid #ccc;
		z-index: -1;
		/* 按需定义 */
	}

	.el-col {
		margin: 3px;
	}

	/* 拖拽相关样式 */
	/*包围div样式*/
	.box {
		width: 100%;
		height: 100%;
		overflow: hidden;
	}

	/*左侧div样式*/
	.mid {
		/* width: calc(32% - 10px); */
		width: 0%;
		/*左侧初始化宽度*/
		height: 100%;
		background: #FFFFFF;
		float: left;
		box-shadow: rgba(0, 0, 0, 0.06) 3px 0px 4px 0px inset;
	}

	.mid1 {
		/* z-index:2;	 */
		/* width: calc(32% - 10px); */
		width: 0%;
		/*左侧初始化宽度*/
		height: 40%;
		background: #FFFFFF;
		float: left;
		box-shadow: rgba(0, 0, 0, 0.06) 3px 0px 4px 0px inset;
	}

	/*拖拽区div样式*/
	.resize {
		cursor: col-resize;
		float: left;
		position: relative;
		top: 45%;
		background-color: #d6d6d6;
		border-radius: 5px;
		margin-top: -10px;
		width: 10px;
		height: 50px;
		background-size: cover;
		background-position: center;
		/*z-index: 99999;*/
		font-size: 32px;
		color: white;
	}

	/*拖拽区鼠标悬停样式*/
	.resize:hover {
		color: #444444;
	}

	/*右侧div'样式*/
	.left {
		float: left;
		/* width: 68%; */
		width: 100%;
		/*右侧初始化宽度*/
		height: 100%;
		background: #fff;
		padding: 0;
	}

	/*ai助手'样式*/
	.v-enter-active,
	.v-leave-active {
		transition: opacity 0.5s ease;
	}

	.v-enter-from,
	.v-leave-to {
		opacity: 0;
	}

	.el-header {
		margin-top: 20px;
	}

	.el-main {
		padding: 0.3375rem 0.9375rem;
	}

	p {
		margin-bottom:10px;
		text-align: left;
		font-size: 0.825rem;
		letter-spacing: 0.15rem;
		font-family: "Helvetica Neue", Helvetica, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "微软雅黑", Arial, sans-serif;
	}

	.btn_p_nob {
		text-align: left;
		font-size: 0.825rem;
		/* letter-spacing: 0.15rem; */
		font-family: "Helvetica Neue", Helvetica, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "微软雅黑", Arial, sans-serif;

	}

	.btn_p {
		text-align: left;
		font-size: 0.825rem;
		letter-spacing: 0.15rem;
		line-height: 1.5;
		font-family: "Helvetica Neue", Helvetica, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "微软雅黑", Arial, sans-serif;
		padding: 0.3125rem 0.25rem;
		border-radius: 0.25rem;
		border: 1px solid #9a9a9a;
		margin: 0.2875rem 0rem;
		transition: font-size 0.3s;
	}

	.btn_p:hover {
		cursor: pointer;
		font-size: 0.80rem;

	}

	span {
		text-align: left;
		/* 没起作用 */
		font-size: 0.725rem;
		letter-spacing: 0.15rem;
		font-family: "Helvetica Neue", Helvetica, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "微软雅黑", Arial, sans-serif;
	}

	.title {
		margin: 0;
		width: 50%;
	}


	.el-row {
		width: 100%;
		padding: 0px;
		margin-bottom: 0.1975rem;
	}

	/*ai助手区*/
	.message-list {
		margin-bottom: 20px;
	}

	.el-avatar {
		background-color: aliceblue;

	}

	.message-item-MY {
		box-shadow: rgba(0, 0, 0, 0.16) 0px 0px 4px;
		/* 	background-color: #66a3ff; */

		overflow: hidden;
		padding: 0.25rem 0.3525rem;
		border: 1px solid #737373;
		border-radius: 0.4125rem 0.4125rem 0rem 0.4125rem;
		margin: 1.3rem 1rem;
	}

	.message-item-AI {
		box-shadow: #66a3ff 0px 0px 1px;

		overflow: hidden;
		padding: 0.25rem 0.3525rem;
		border: 1px solid #737373;
		/* border-radius: 0.3125rem; */
		border-radius: 0.4125rem 0.4125rem 0.4125rem 0rem;
		margin: 0.725rem 1rem;
	}

	.el-footer {
		position: inherit;
		width: 100%;
		margin-top: 0.625rem;
		bottom: 0;
		min-height: 6.5rem;
		max-height: 10rem;
	}

	.footer-left {
		float: left;
		width: 90%;
	}

	.footer-right {
		float: right;
		width: calc(10%-3px);
		margin-left: 2px;
	}

	/*右边侧边栏功能区 */
	.bg-right {
		display: flex;
		align-items: top;
		/* box-shadow: rgba(0, 0, 0, 0.06) 3px 0px 2px 0px inset; */
		border-left: #d6d6d6 1px solid;
	}

	.buttonAI {
		padding: 0.25rem 0.0625rem;
	}

	.buttonAI:hover {
		background-color: #f8f7ff;
	}

	/* 提示词模板相关样式 */
	.el-select {
		width: 90%;
	}

	/*教案大纲*/
	#header-container {
		list-style-type: none;
		 padding-left: 20px;

	}
	#header-container li {
		margin-top: 20px;
		color: #33081b;
		margin: 10px 0;
		cursor: pointer;
		border: #bfbfbf 1px solid;
		border-radius: 0.3125rem;
		font-size: 2.5625rem;
		
	}

	#header-container li:hover {
		text-decoration: underline;
		background-color: #66a3ff;
	}

	#header-container li[type="header1"] {
		font-size: 20px;
		font-weight: bold;
		
	}

	#header-container li[type="header2"] {
		font-size: 16px;
		padding-left: 15px;
		font-weight: bold;
	}

	#header-container li[type="header3"] {
		font-size: 14px;
		padding-left: 30px;
	}

	#header-container li[type="header4"] {
		font-size: 12px;
		padding-left: 45px;
	}

	#header-container li[type="header5"] {
		font-size: 12px;
		padding-left: 60px;
	}
    /* 提示词模板样式*/
	.prom{
		border: 1px solid #cfcfcf;
		border-radius: 0.125rem;
		padding: 0.4125rem 0.3125rem;
	}
	
</style>