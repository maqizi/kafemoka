<template>
	<div class="bg">
	<el-row v-if="!isButtonHidden">
		<p>请先选择您的教学科目：</p>
	</el-row>
	<el-row :gutter="20" v-if="!isButtonHidden">
	<el-radio-group v-model="radio">
		<el-col :span="8" v-for="(subject, index) in subjects" :key="index">
		    <el-radio-button v-model="radio" :label="subject.text" >{{subject.text}}</el-radio-button> 
		</el-col>
	</el-radio-group>
	</el-row>
	<el-row><el-button @click="shuffleButtons" v-if="!isButtonHidden">点击我为您设计任务</el-button></el-row>
	<el-row v-if="isButtonHidden"><p>请按照以下顺序开始您的实验吧！<span class="animate__animated animate__flash animate__infinite">_</span></p></el-row>
	<el-row :gutter="20" v-if="isButtonHidden">
	<el-col :span="6" v-for="(button, index) in shuffledButtons" :key="index">  
	    <el-button class="animate__animated animate__fadeIn shadowBox" @click="gotoStudy(button.path,index)">{{ button.text }}</el-button>  
    </el-col> 
	</el-row>
	
	<el-row :gutter="20" v-if="isButtonHidden">
		<el-col :span="6" v-for="(Theme, index) in matchTheme" :key="index">
		    <el-button class="animate__animated animate__fadeIn shadowBox" disabled>{{ Theme }}</el-button>  
		</el-col>
		
	</el-row>
	<p>每个教案任务分别对应每个实验，请放心，进入每个实验环境之后依然会有提示对应的教案任务。</p>
	</div>
</template>

<script>
	export default {  
	  data() {  
	    return {
		  radio:'语文',
		  subjects:[{
			text:'语文',
			theme:['春/朱自清1','春/朱自清2','春/朱自清3','春/朱自清4'],
		  },{
			 text:'数学',
			 theme:['1','2','3','4'], 
		  },{
			 text:'英语',
			 theme:['1','2','3','4'],  
		  }],
		  buttons:[{
			text:'实验1',
			path:'studyNo_1'
		  },
		  {
			text:'实验2',
			path:'studyNo_2'
		  },
		  {
			text:'实验3',
			path:'studyNo_3'
		  },
		  {
			text:'实验4',
			path:'studyNo_4'
		  }],// 原始按钮数组  
	      shuffledButtons: [], // 打乱后的按钮数组  
		  isButtonHidden:false,
		  matchTheme:[],
		  
	    };  
	  },  
	 mounted() {
	 	//在该mounted中获取教师数据库中是否已经经历了shuffleButtons
		//1-先获取当前教师的名字
		const user_name = sessionStorage.getItem('user_name');
		//2-根据当前教师的userName获取是否已经经历了shuffleButtons，是的话，isButtonHidden=true， study1 study2 study3 study4为数据库来的数据

		//再根据得来的数据对shuffleButtons进行赋值，比如[this.buttons[i-1],this.buttons[j-1],this.button[k-1],this.buttons[g-1]]
		//study1C study2C study3C study4C 若为1，则true，0为false

	 },
	  methods: {  
		
	    shuffleButtons() {  
		  this.isButtonHidden=true;
	      // Fisher-Yates shuffle algorithm  生成一个随机排列的算法
	      for (let i = this.buttons.length - 1; i > 0; i--) {  
	        const j = Math.floor(Math.random() * (i + 1)); // 随机索引  
	        [this.buttons[i], this.buttons[j]] = [this.buttons[j], this.buttons[i]]; // 交换元素  
	      }  
	      this.shuffledButtons = [...this.buttons]; // 复制数组到 shuffledButtons 以保持响应性  
		  for(var i=0;i<this.subjects.length;i++){
			  if(this.subjects[i].text===this.radio){
				  this.matchTheme=this.subjects[i].theme;
				  console.log(this.matchTheme);
				  break;
			  }
		  }
		  // 使用map方法提取text的最后一个字符并转换为数字
		  let numbers = this.shuffledButtons.map(button => parseInt(button.text.slice(-1), 10)); 
		  console.log(numbers);
		  //数据库：把实验顺序存入教师档案中
		  
		  
	    },
		gotoStudy(path,index){
			const m=this.matchTheme[index];
			if(path=='studyNo_1'||path=='studyNo_2'){
				this.$router.push({name:path,
								    params:{
									matchTheme:m,
									}
				});
			}else{
				this.$router.push({name:'Inputinfo',
								    params:{
									path:path,
									matchTheme:m,
									}
				});
				
			}
			
		},  
		  
	  },  
	};  
	
</script>

<style scoped>
	.bg {  
	  width: 100%;
	  height: 100%;
	  /* background-image: url(../assets/Maldives.png); */
	  background: linear-gradient(to top,  #fff,rgb(190, 227, 255));
	  /* background-color: #acd1fd; */
	  background-size: 100% 100%;
	  background-repeat: no-repeat;
	  display: flex;
	  align-items: center;
	  padding-top: 10%;
	 /* justify-content: center; */
	  flex-direction: column;
	}  
	.el-row {
	    margin-bottom: 20px;
	    &:last-child {
	      margin-bottom: 0;
	    }
	  }
	  p{
		  margin-bottom:17px;
		  font-size: 1.15rem;
	  }
	  .shadowBox{
		  box-shadow: rgba(85, 85, 255, 0.1) 0px 5px 15px 0px;
		  border:0px;
		  border-radius:7px;
	  }
	 

</style>