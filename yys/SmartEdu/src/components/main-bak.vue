<template>
	<el-container style="height: 700px; border: 1px solid #eee">
	
		<el-header style="text-align: right; font-size: 18px">
			<el-button icon="el-icon-share"  @click="dialogFormVisible = true">分享</el-button>
			<el-dialog title="教案分享" :visible.sync="dialogFormVisible">
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
			
			<el-button icon="el-icon-download"  @click="dialogdownload = true">下载</el-button>
			<el-dialog title="教案下载" :visible.sync="dialogdownload">
				<el-button icon="el-icon-download" >PDF下载</el-button>
				<el-button icon="el-icon-download" >WORD下载</el-button>
				<div slot="footer" class="dialog-footer">
				  <el-button @click="dialogdownload = false">取 消</el-button>
				  <el-button type="primary" @click="dialogdownload = false">确 定</el-button>
				</div>
			</el-dialog>
			<!-- <router-link to="/Etherpad">跳转到分享</router-link> -->
			<el-button icon="el-icon-coin"  @click="saveedu()">保存</el-button>
			<el-button icon="el-icon-user" circle ></el-button>
			
		</el-header>
	 
	
	  <el-container>
		<el-aside width="200px" style="background-color: rgb(238, 241, 246)" id="Navigation">
			<el-row class="tac">
			  <el-col :span="24">
				<h5>导航栏</h5>
				<el-menu class="el-menu-vertical-demo" background-color="#fff6f6" text-color="#000000">
				  <el-menu-item index="1">
					<i class="el-icon-menu"></i>
					<span slot="title">教材分析</span>
				  </el-menu-item>
				  <el-menu-item index="2">
					<i class="el-icon-menu"></i>
					<span slot="title">学情分析</span>
				  </el-menu-item>
						<el-menu-item index="3">
						  <i class="el-icon-menu"></i>
						  <span slot="title">教学目标</span>
						</el-menu-item>
						<el-menu-item index="4">
						  <i class="el-icon-menu"></i>
						  <span slot="title">教学重点</span>
						</el-menu-item>
						<el-menu-item index="5">
						  <i class="el-icon-menu"></i>
						  <span slot="title">教学过程</span>
						</el-menu-item>
						<el-menu-item index="6">
						  <i class="el-icon-menu"></i>
						  <span slot="title">学习评价</span>
						</el-menu-item>
				  
				</el-menu>
			  </el-col>
			</el-row>
	
		</el-aside>
			
		<el-main style="background-color: rgb(255, 255, 255)" id="Lessoncontent">
			<!-- <div contenteditable="true" id = "LessonName" class="LessonName">教案名称</div>
			<div contenteditable="true" id = "Lessoncontent" class="Lessoncontent">教案内容</div> -->
	
			<el-card class="box-card" id = "LessonName">
				<div contenteditable="true">教案名称</div>
			</el-card>
	
			<el-card class="box-card" id = "Lessoncontent">
				<div contenteditable="true">教案内容</div>
			</el-card>
			
		
		
		  <!-- <el-header style="height:auto">
				<el-card class="box-card" id = "LessonName">
					<h1>观潮</h1>
				</el-card>
		  </el-header>
		  <el-main>
				<el-card class="box-card" id = "TeachingContent">
					<h1 style="text-align: left">教材分析</h1>
					<p style="text-align: left">
						《观潮》是人教版小学语文六年制第7册第一组的一篇课文，本组课文以“大自然的魅力”为主题，为我们编选了4篇课文，本篇课文叙述的是一次观潮的盛况，写的是作者耳闻目睹的潮来前、潮来时、潮头过后的景象，描写了大潮有远而近，奔腾西去的全过程，描绘出江潮由风平浪静到奔腾咆哮再到又恢复平静的动态变化，写出了大潮的奇特、壮观和雄伟。
						课文结构清晰，层次分明，文中作者不但运用比喻的手法直接描写了潮水汹涌澎湃、雷霆万钧的气势和声威，还从观潮人数之多，热情之高间接的反映了大潮的奇特，使人读后不禁由衷的发出了“钱塘江大潮，真不愧为自古以来的天下奇观。”编选本篇课文的意图有二，一是使学生通过阅读感受钱塘江大潮的奇特，激发学生热爱大自然、热爱祖国大好河山的情感，二是引导学生一边读书一边想象画面，并通过品味关键词句、重点段落，体会课文在表达上的特点。
					</p>
				</el-card>
				
				<el-card class="box-card" id = "SituationAnalysis">
					<h1 style="text-align: left">学情分析</h1>
					<p style="text-align: left">
						对于刚步入四年级的学生而言，他们虽然对于写景文章有初步的认识，但他们在联系上下文、理解词句的意思，抓住关键词句，体会其在表达情意方面的作用上还是存在较大的难度。此外，钱塘江大潮离学生的生活实际较远，学生较难感受体会其奇特、壮观的景色，这就要求教师创设好情景，设计好句子理解的坡度，激发学生的想象，引领学生走进文本，感知大潮的奇特、壮观、雄伟。
					</p>
				</el-card>
				
				<el-card class="box-card" id = "TeachingObjectives">
					<h1 style="text-align: left">教学目标</h1>
					<p style="text-align: left">
						1.通过联系上下文、查阅相关资料，学会“潮、称、盐”等13个生字，认识“罩、屹、鼎”等7个生字，正确读写“宽阔、笼罩、薄雾、屹立、若隐若现、山崩地裂、齐头并进、漫天卷地”等词语。
						2.通过“三读（读准、读通、读懂）”，自主学习，乐于朗读，做到正确、流利、有感情的朗读课文。背诵课文3、4自然段。
						3.边读边想象画面，能联系上下文、生活实际理解体会词句的含义。
						4.感受钱塘江大潮的奇特、壮观，感受大自然的魅力，受到自然美的熏陶，并能把自己的阅读感受与他人交流。
					</p>
				</el-card>
				
				<el-card class="box-card" id = "TeachingImportant">
					<h1 style="text-align: left">教学重点</h1>
					<p style="text-align: left">
						引导学生在入情入境的阅读中，体会感受钱塘江大潮的奇特壮观。
						体会文中的有关词句，想象课文描写的大潮的景色。
					</p>
				</el-card>
				
				<el-card class="box-card" id = "TeachingProcess">
					<h1 style="text-align: left">教学过程</h1>
					<p style="text-align: left">
					</p>
				</el-card>
				
				<el-card class="box-card" id = "LearningEvaluation">
					<h1 style="text-align: left">学习评价</h1>
					<p style="text-align: left">
					</p>
				</el-card>
	
				<el-card class="box-card" id = "Homework">
					<h1 style="text-align: left">课后作业</h1>
					<p style="text-align: left">
					</p>
				</el-card>
				
		  </el-main> -->
			  
		</el-main>
		
	
		
	  </el-container>
	
	</el-container>
	</template>
	
	<style>
	  .el-header {
		background-color: #ffffff;
		color: #333;
		line-height: 60px;
	
	  }
	  
	  .el-aside {
		color: #333;
	  }
	  
	  .box-card {
		width: auto;
		background-color: rgb(255, 247, 247);
	  }
	
	  /* .el-button{
		background-color: rgb(255, 247, 247);
	  } */
	 
	
	</style>
	
	<script>
	import {nInsertlesson} from '../api/api.js'
	 export default {
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
			 formLabelWidth: '120px',
			 LessonName: '',
			 Lessoncontent:'',
			
		   };
		 },
		 methods: {
			saveedu() {
				sessionStorage
				const user_name = sessionStorage.getItem('user_name');
				// const user_name = localStorage.getItem('user_name');
				var LessonName = document.getElementById("LessonName").innerText;
				var Navigation = document.getElementById("Navigation").outerHTML;
				var Lessoncontent = document.getElementById("Lessoncontent").outerHTML;
				
	
				nInsertlesson(user_name, LessonName, Navigation, Lessoncontent).then(response => {
	
					if(response.data.status == true){
						// 注册成功，显示成功框
						this.$message({
								message: '保存成功',
								type: 'success'
								});
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
				lessonshare(){
					this.$message({
								message: '分享成功',
								type: 'success'
								});
				},
				
			}
	   };
	  
	</script>