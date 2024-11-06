<template>
	<div>
		<el-header style="text-align: right; font-size: 18px">
		<el-button icon="el-icon-share" type="text" @click="dialogFormVisible = true">分享</el-button>
		<el-dialog title="教案分享" :visible.sync="dialogFormVisible" width="30%">
		  <el-form :model="form">
		    <el-form-item label="添加用户ID" :label-width="formLabelWidth">
		      <el-input v-model="form.name" autocomplete="off"></el-input>
		    </el-form-item>
		    <el-form-item label="用户权限:" :label-width="formLabelWidth">
		      <el-select v-model="form.region" placeholder="请选择用户权限">
		        <el-option label="查看" value="shanghai"></el-option>
		        <el-option label="评论" value="beijing"></el-option>
				<el-option label="编辑" value="beijing"></el-option>
		      </el-select>
		    </el-form-item>
		  </el-form>
		  <div slot="footer" class="dialog-footer">
		    <el-button @click="dialogFormVisible = false">取 消</el-button>
		    <el-button type="primary" @click="dialogFormVisible = false">确 定</el-button>
		  </div>
		</el-dialog>
		
		<el-button icon="el-icon-download" type="text" @click="dialogdownload = true">下载</el-button>
		<el-dialog title="教案下载" :visible.sync="dialogdownload" width="30%">
			<el-button icon="el-icon-download" >PDF下载</el-button>
			<el-button icon="el-icon-download" >WORD下载</el-button>
			<div slot="footer" class="dialog-footer">
			  <el-button @click="dialogdownload = false">取 消</el-button>
			  <el-button type="primary" @click="dialogdownload = false">确 定</el-button>
			</div>
		</el-dialog>
		<!-- <router-link to="/Etherpad">跳转到分享</router-link> -->
		<el-button icon="el-icon-coin" type="text" @click="saveedu()">保存</el-button>
		<el-button icon="el-icon-user" circle ></el-button>
		
    </el-header>

		<el-row type="flex" class="row-bg" justify="space-between">
			<el-col class="col01" :sm="1" :md="3" :lg="3" :xl="3">

				<!-- <p>test1</p>
				<el-button @click="selectInsert">按下这个更改文字</el-button>
				<el-divider></el-divider>
				<p>test2</p>
				<el-button @click="generateTextStream">测试ai生成教案</el-button>
				<p>{{$store.state.Lesson.Les.lcontent}}</p>
				<p>test3</p>
				<el-button @click="insertResume">测试插入新定义节点node</el-button> -->
				<!-- 标题目录 -->
				<!-- <el-button @click="insertResume">测试插入新定义节点node</el-button>
				<el-button @click="nav">测试定位</el-button> -->

				<!-- <div style="width: 200px; background-color: #f1f1f1;">
					<ul id="header-container" @click="navId"></ul>
				</div> -->

				<!-- <p>{{Les}}</p> -->
				<!-- <p>test3</p>
				<el-button @click="editLes">点击执行修改操作：mutation(用commit)</el-button>
				<p>test4</p>
				<el-button @click="editLes1">点击执行修改操作：action(用dispatch)</el-button> -->
				<!-- <el-button @click="addStyle">测试加样式</el-button>
              <el-button @click="generateTextStream">测试ai生成教案</el-button> -->
			</el-col>
			<el-col :sm="22" :md="20" :lg="20" :xl="20">
				<div class="box" ref="box">
					<div class="left">
						<!--左侧div内容-->
						<div>

							<!-- 工具栏 -->
							<Toolbar :editor="editor" :defaultConfig="toolbarConfig" />
							<!-- 编辑器 -->
							<Editor id="content" style="height:85vh;overflow-y: auto;" :defaultConfig="editorConfig"
								v-model="html" @onChange="onChange" @onCreated="onCreated" v-katex:auto />
							<div style="width: 180px;  position: absolute;left: 0;top: 30%;"  >
								<ul id="header-container" ></ul>
								
							</div>
							 


						</div>
					</div>
					<div class="resize" title="收缩侧边栏" v-show="AIVisual||PromptStoreVisual">
						⋮
					</div>
					<!-- AI助手显示区域 -->
					<div class="mid" v-show="AIVisual">
						<!--右侧div内容:用于显示ai助手界面-->

						<div>
							<el-container>
								<el-header><el-button type="primary" round size="small"
										class="title">教案AI助手</el-button></el-header>
								<el-main>
									<el-scrollbar wrap-class="message-list" wrap-style="height:30rem;">
										<div v-for="(message, index) in messages" :key="index"
											:class="{'message-item-AI':message.sender=='AI', 'animate__animated animate__fadeInUp':true,'message-item-MY':message.sender=='MY'}">
											<div v-if="message.sender=='AI'" style="float:left;margin-right: 0.4rem;">
												<el-avatar :size="40" :src="img_AI"></el-avatar>
											</div>
											<div>
												<p v-if="message.sender=='MY'"> {{ message.content }}</p>
												<div v-if="message.sender=='AI'"
													style="overflow: hidden;padding-top:3px;">

													<div class="btn_p_nob" v-if="message.content[0]!=''">原来的文本:<br>
														<p class="btn_p" @click="selectInsert(message.content[0])">
															{{message.content[0]}}
														</p><br>生成的文本:
													</div>
													<div :class="{'btn_p':message.content[0]!=''}">
														<p @click="selectInsert(message.content[1])"
															v-html="message.content[1]"></p>
														<i v-if="message.content[0]!=''" class="el-icon-refresh"
															@click="updateMessage"></i>
													</div>

												</div>
											</div>
											<div v-if="message.sender=='MY'"
												style="float: right;margin-left: 0.3125rem;"><el-avatar :size="40"
													:src="img_MY"></el-avatar></div>
										</div>
									</el-scrollbar>
								</el-main>
								<!-- 教师输入 -->
								<el-footer>
									<!-- 教师输入-左侧：输入文本 -->
									<div class="footer-left">
										<el-input v-model="inputMessage" :placeholder="tip" :rows="4" type="textarea"
											id="voiceTxt"></el-input>
									</div>
									<!-- 教师输入-右侧：发送+语音+提示词库 -->
									<div class="footer-right">
										<el-row>
											<el-popover placement="right" trigger="hover">
												<!-- <el-select v-model="selectedValue" filterable placeholder="请选择提示词库">
							      <el-option
							        v-for="item in promptBox"
							        :key="item.value"
							        :label="item.label"
							        :value="item.value">
							      </el-option>
							    </el-select> -->
												<!-- <el-divider></el-divider>
							  <el-scrollbar wrap-class="message-list" wrap-style="height:400px;">
							    <div v-for="(prompt, index) in content" :key="index" class="prompt-item">
							      <p> {{ prompt }}</p>
								 <el-divider></el-divider>
							    </div>
							  </el-scrollbar> -->
												<el-button  slot="reference" 
													size="small" style="border: 0px;"></el-button>
											</el-popover>

											</el-popover>
										</el-row>
										<el-row>
											<el-tooltip class="item" effect="dark" content="语音"
												placement="right"><el-button class="el-icon-microphone" circle
													size="small" @click="startVoice"></el-button></el-tooltip>
										</el-row>
										<el-row>
											<el-tooltip class="item" effect="dark" content="发送"
												placement="right"><el-button class="el-icon-s-promotion" circle
													size="small" @click="sendMessage"></el-button></el-tooltip>
										</el-row>
									</div>
								</el-footer>
							</el-container>

						</div>
					</div>

					<!-- AI提示词模板显示区域 -->
					<div class="mid1" v-show="PromptStoreVisual">
						<el-container>
							<el-header><el-button type="primary" round size="small"
									class="title">教案提示词模板</el-button></el-header>
							<el-main>
								<el-select v-model="value9" multiple filterable remote reserve-keyword
									placeholder="请输入关键词" :remote-method="remoteMethod" :loading="loading">
									<!-- <el-option v-for="item in options4" :key="item.value" :label="item.label"
										:value="item.value">
									</el-option> -->
								</el-select>
								<el-scrollbar wrap-class="message-list" wrap-style="height:30rem;margin-top:20px;padding-left:20px;">
									<div v-for="item in options4" :key="item.value" style="margin-top: 10px;;">
										<p> {{ item.value }}</p>
									</div>


								</el-scrollbar>
							</el-main>
							<!-- 教师输入 -->
							<el-footer>
								<!-- 教师输入-左侧：输入文本 -->

							</el-footer>
						</el-container>

					</div>
				</div>
			</el-col>
			<el-col :sm="1" :md="1" :lg="1" :xl="1" class="bg-right">
				<el-row>
					<div class="buttonAI" @click="clickBtnAI"><el-avatar :size="40" :src="img_AI"></el-avatar></div>
					<div class="buttonAI" @click="clickBtnStore"><el-avatar :size="40" :src="img_Store"></el-avatar>
					</div>
				</el-row>

			</el-col>
		</el-row>
	</div>
</template>

<script>
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
	// import conf1 from '../js/renderELem.js'
	// import conf2 from '../js/elem-to-html.js'
	// import conf3 from '../js/parse-to-html.js'
	// import plug from '../js/plugin.js'
	// import {conf1} from '../js/newElem/render-elem.js'
	// import module from '../js/index.js'
	// Boot.registerModule(module);
	import MyButtonMenu from '../js/new_file.js'
	//引入调用科大讯飞语音功能的js文件
	// import Voice from '../js/voice.js'
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
				dialogFormVisible: false,
				dialogdownload: false,
				form: {
				name: '',
				region: '',
				date1: '',
				date2: '',
				delivery: false,
				type: [],
				resource: '',
				desc: ''
				},
				// formLabelWidth: '10px',
				/*测试ai生成教案功能*/
				headerContainer: '',
				outputList: [],
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
						content: ['', '您好呀，我是教案AI助手。您想生成的教案的基本信息为：<br>《观潮》是人教版小学语文六年制第7册第一组的一篇课文']
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
				html: "<h1>标题</h1><h2>标题A</h2><p>文本</p><p>文本</p><p>文本</p><h3>标题A1</h3><p>文本</p><p>文本</p><p>文本</p><h3>标题A2</h3><p>文本</p><p>文本</p><p>文本</p><h2>标题B</h2><p>文本</p><p>文本</p><p>文本</p><h3>标题B1</h3><p>文本</p><p>文本</p><p>文本</p><h3>标题B2</h3><p>文本</p><p>文本</p><p>文本</p> ",
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
							menuKeys: ['MyButtonMenu', '|', 'headerSelect', 'bold', 'underline', 'italic', '|', 'fontSize',
								'fontFamily',
							], // 定义你想要的 menu keys'MyButtonMenu',
						}
					},

					// 所有的菜单配置，都要在 MENU_CONF 属性下
					MENU_CONF: {},
				},
				// 提示词模板相关变量
				options4: [],
				value9: [],
				list: [],
				loading: false,
				states: ["这一部分是否有遗漏或不准确的地方。", "是否存在逻辑上的跳跃或不一致之处？", "提示词3",
					"提示词4", "提示词5", "提示词6",
					"提示词7", "Delaware", "Florida",
					"Georgia", "Hawaii", "Idaho", "Illinois",
					"Indiana", "Iowa", "Kansas", "Kentucky",
					"Louisiana", "Maine", "Maryland",
					"Massachusetts", "Michigan", "Minnesota",
					"Mississippi", "Missouri", "Montana",
					"Nebraska", "Nevada", "New Hampshire",
					"New Jersey", "New Mexico", "New York",
					"North Carolina", "North Dakota", "Ohio",
					"Oklahoma", "Oregon", "Pennsylvania",
					"Rhode Island", "South Carolina",
					"South Dakota", "Tennessee", "Texas",
					"Utah", "Vermont", "Virginia",
					"Washington", "West Virginia", "Wisconsin",
					"Wyoming"
				],




			}
		},
		watch: {
			output() {

				//改变策略
				this.html = `<h4 id="hello">hello</h4><p>${this.output}</p>`;

			},
			outcome() {
				this.come = this.outcome;
			}
		},
		mounted() {
			//寻找header标签并且得到对应的id成为大纲
			this.headerContainer = document.getElementById('header-container')
			    this.headerContainer.addEventListener('mousedown', event => {
			      if (event.target.tagName !== 'LI') return
			      event.preventDefault()
			      var id = event.target.id
				  console.log(id);
			      this.editor.scrollToElem(id) // 滚动到标题
			    })
			//提示词模板搜索相关提示词
			this.list = this.states.map(item => {
				return {
					value: item,
					label: item
				};
			});
			this.dragControllerDiv();
			//start：这里是把语音功能实例化
			let times = null;
			const voiceTxt = document.querySelector('#voiceTxt'); //采用dom方式可操作教师输入框，否则，当text改变时，教师输入框可不会自动更新
			this.voice = new Voice({ //实例化为voice

				// 服务接口认证信息 注：apiKey 和 apiSecret 的长度都差不多，请要填错哦，！
				appId: '66009497',
				apiSecret: 'OTJkNGQ2MjM1NjU3ZGMyYmE0ZDcyZjBh',
				apiKey: '3eebcad1e6d109a9cf99e25f979f285d',
				// 注：要获取以上3个参数，请到迅飞开放平台：https://www.xfyun.cn/services/voicedictation 【注：这是我的迅飞语音听写（流式版）每天服务量500（也就是调500次），如果你需求里大请购买服务量：https://www.xfyun.cn/services/voicedictation?target=price】

				onWillStatusChange: function(oldStatus, newStatus) {
					//可以在这里进行页面中一些交互逻辑处理：注：倒计时（语音听写只有60s）,录音的动画，按钮交互等！
					//fixed-box（开始录音之后显示录音麦克风div）
					//fixedBox.style.display = 'block';
				},
				onTextChange: function(text) {
					//监听识别结果的变化
					voiceTxt.value = text;
					this.inputMessage = text;
					console.log("text:" + voiceTxt);

					// 3秒钟内没有说话，就自动关闭
					if (text) {
						clearTimeout(times);
						times = setTimeout(() => {
							this.stop(); // voice.stop();
							this.VoiceClick = false;
							//fixedBox.style.display = 'none';
						}, 3000);
					};
				}
			});
			//end：语音功能实例化结束
			// start：这里是把ai编辑的菜单注册到wangeditor中
			let that = this;
			class My1 extends MyButtonMenu {
				exec(editor, value) {
					// that.tip='更改文本'+'" '+value.toString().substring(0,60)+' "';
					//that.tipAdress=that.editor.selection;
					that.clickBtnAI();
				}
			};
			const menu1Conf = {
				key: 'MyButtonMenu', // 定义 menu key ：要保证唯一、不重复（重要）
				factory() {
					return new My1 // 把 `YourMenuClass` 替换为你菜单的 class 
				}
			};


			const module = { // TS 语法
				// const module = {                      // JS 语法

				menus: [menu1Conf], // 菜单
				// editorPlugin: withBreakAndDelete, // 插件
				// renderElems: [conf1, /* 其他元素... */] ,// renderElem
				// elemsToHtml: [conf2, /* 其他元素... */]  ,// elemToHtml
				// parseElemsHtml: [conf3, /* 其他元素... */]  ,// parseElemHtml
				// editorPlugin: plug,

				// 其他功能，下文讲解...
			}
			Boot.registerModule(module)

			//Boot.registerMenu(menu1Conf);

			//end：wangeditor注册新菜单（ai编辑）结束
			// 模拟 ajax 请求，异步渲染编辑器
			// let len=0;
			// let timerId = setInterval(() => {
			//     if (this.output.length > len) {
			//         console.log("html:" + this.html);
			//         this.html = `${this.output}`;

			//     } 
			// }, 1500);


		},
		created() {

		},

		methods: {
			addStyle(){
				
			},
			insertResume() {

				// let resume = { // JS 语法
				// 	type: 'h4',
				// 	title: 'resume.pdf',
				// 	content: 'https://xxx.com/files/resume.pdf',
				// 	children: [{
				// 		text: ''
				// 	}] // void 元素必须有一个 children ，其中只有一个空字符串，重要！！！
				// }
				// let resume = { // JS 语法
				// 	type: 'header4',
				// 	children: [{
				// 		text: '教学内容'
				// 	}] ,// void 元素必须有一个 children ，其中只有一个空字符串，重要！！！,
				// 	id:'re'
				// }
				// this.editor.insertNode(resume);



			},
			
			// editLes(){
			// 	const Les={
			// 		lcontent: '4',
			// 		lobjective:'3',
			// 		lanalysis:'2',
			// 		lpoint:'1',
			// 		lprodure:'0'
			// 	}
			// 	this.$store.commit('Lesson/changeLes',Les);
			// },
			// editLes1(){
			// 	const Les={
			// 		lcontent: '4',
			// 		lobjective:'3',
			// 		lanalysis:'2',
			// 		lpoint:'1',
			// 		lprodure:'0'
			// 	}
			// 	this.$store.dispatch('Lesson/actChangeLes',Les);
			// },
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
				console.log("触发了clickbtnai");
				var resize = document.getElementsByClassName('resize');
				var left = document.getElementsByClassName('left');
				var mid = document.getElementsByClassName('mid');
				if (!this.AIVisual) {
					this.AIVisual = true;
					console.log(this.AIVisual);
					left[0].style.width = 68 + '%';
					mid[0].style.width = 'calc(' + 32 + '% - ' + 10 + 'px)';
				} else {
					this.AIVisual = false;
					console.log(this.AIVisual);
					mid[0].style.width = 0 + '%';
					left[0].style.width = 100 + "%";
				}

			},
			//点击buttonAI把mid宽度修改为0%，left宽度为100%
			clickBtnStore() {
				console.log("触发了PromptStoreVisual");
				var resize = document.getElementsByClassName('resize');
				var left = document.getElementsByClassName('left');
				var mid = document.getElementsByClassName('mid1');
				if (!this.PromptStoreVisual) {
					this.PromptStoreVisual = true;
					console.log(this.PromptStoreVisual);
					left[0].style.width = 68 + '%';
					mid[0].style.width = 'calc(' + 32 + '% - ' + 10 + 'px)';
				} else {
					this.PromptStoreVisual = false;
					console.log(this.PromptStoreVisual);
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
			insertNewNode() {
				// var cardElement = {
				// 	type: 'card1',
				// 	children: [{
				// 		type: 'header3',
				// 		children: [{
				// 			text: '教学内容',
				// 		}]
				// 	}, {
				// 		type: 'paragraph',
				// 		children: [{
				// 			text: this.output //测试是否会自动更新
				// 		}]
				// 	}],
				// };
				// this.editor.insertNode(card);
				// console.log(this.editor.children)

			},
			selectInsert(changeText) {

				this.editor.select(this.tipAdress)
				this.editor.dangerouslyInsertHtml(changeText);
				// this.editor.dangerouslyInsertHtml('<p style="text-align:left;border:2px solid #ff5500;">hello</p>');
			},
			handleEnter() {
				console.log('按钮被点击了');
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

				console.log("this.selectStr:" + this.selectStr);

				this.tip = '更改文本' + '" ' + editor.getSelectionText().toString().substring(0, 60) + '"'; //显示输入框提示文本
				// editor.insertText('xxx');出现卡顿错误
				this.selectStr = editor.getSelectionText();
				console.log('onChange', editor.getHtml()) // onChange 时获取编辑器最新内容
				const headerContainer = document.getElementById('header-container')
				const headers = editor.getElemsByTypePrefix('header')
				headerContainer.innerHTML = headers.map(header => {
					let i=1;
					const text = SlateNode.string(header)
					console.log(text)
					const {
						id,
						type
					} = header
					 return `<li id="${id}" type="${type}" style='padding: 10px 0px;color: #33081b;cursor: pointer;border: #bfbfbf 1px solid;border-radius: 0.3125rem;font-size:13px;'><i class="el-icon-menu" style="margin-right:5px;"></i>${text}</li>`
				}).join('')


			},
			getEditorText() {
				const editor = this.editor;
				if (editor == null) return;

				console.log('getEditorText', editor.getText()); // 执行 editor API
			},
			printEditorHtml() {
				const editor = this.editor;
				if (editor == null) return;

				console.log(editor.getHtml()); // 执行 editor API
			},
			//ai流式生成教案
			async generateTextStream() {
				// this.insertNewNode();
				const sys = `你是教学设计机器人，我将提供教学信息给你，你的工作是为老师设计一份教案.`;
				const us = `教学信息在以下三个反引号（\`\`\`）内：\n\`\`\`\n ${this.LesInfo.lname} 五年级 小学 语文\n\`\`\`\``;

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
					this.output += output_str.replace(/\n/g, "<br>", ); //对于ai生成的东西进行处理，由于字符串中的/n表示换行+空一行，而<br>可以只换行
					output_str = '';
					//console.log(this.output);
				}
				// this.insertNewNode();

			},
			//ai逐句修改补充
			async generateTextStreamToParagraph() {

				this.outcome = ''; //将上一次ai获得的答案进行清空
				const selectStr = this.selectStr;
				const sys = `你是一个专业的教案修改机器人。请你根据我提出的需求修改并且完善我选中的一段话。请注意，输出修改的内容即可，无需其他话语，字数规定与原来的字数差不多。`;
				const us = `我选中的一段话是${selectStr}.修改要求是${this.inputMessage}.`;

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
					this.outcome += output_str.replace(/\n/g, "<br>", ); //对于ai生成的东西进行处理，由于字符串中的/n表示换行+空一行，而<br>可以只换行
					output_str = '';
					//console.log(this.outcome)
					//console.log(this.output);
				}

				//生成且更新教师要求的信息
				let length = this.messages.length;
				let last = this.messages[length - 1];
				console.log(last);
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
			}



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
</style>