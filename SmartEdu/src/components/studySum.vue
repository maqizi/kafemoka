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
	<el-row><el-button @click="shuffleButtonsa" v-if="!isButtonHidden">点击我为您设计实验任务</el-button></el-row>
	<el-row v-if="isButtonHidden"><p>请按照以下顺序开始您的实验吧！一共有四个实验条件<span class="animate__animated animate__flash animate__infinite">_</span></p></el-row>
	<el-row :gutter="20" v-if="isButtonHidden">
	<el-col :span="6" v-for="(button, index) in shuffledButtons" :key="index">  
	    <el-button class="animate__animated animate__fadeIn shadowBox" @click="gotoStudy(button.path,index)" :disabled="!button.completed">{{ button.text }}</el-button>  
    </el-col> 
	</el-row>
	
	<el-row :gutter="20" v-if="isButtonHidden">
	<p>为您分配好了每个实验条件的教案任务，请根据以上实验条件顺序开始实验，请放心，进入对应的实验中，依然会有提示提醒对应实验条件的教案任务。</p>
	<el-col :span="6" v-for="(Theme, index) in matchTheme" :key="index">  
	    <div class="animate__animated animate__fadeIn shadowBox" >{{ Theme }}</div>  
	</el-col> 
	</el-row>
	</div>
</template>

<script>
import {insertstudyorder,insertstudyorderc,insertstudtime,inserthistoryc,inserthistoryaia,getstudyorder,getstudyorderc,getuserid,getsubjectnum} from '../api/api.js'
	export default {  
	  data() {  
	    return {
		  radio:'语文',
		  subjects:[{
			text:'语文',
			theme:['纪念白求恩/毛泽东','渡荆门送别/李白','生于忧患，死于安乐《孟子三章》','《乡愁》/余光中'],
		  },{
			 text:'数学',
			 theme:['正数和负数','消元——解二元一次方程组','平方差公式','中心对称图形'], 
		  },{
			 text:'英语',
			 theme:['Good morning！','what color is it?','I‘m more outgoing than my sister','what‘s the best movie theater?'],  
		  }],
		  buttons:[{
			text:'条件1：纯文本编辑器',
			path:'studyNo_1',
			completed:true,
		  },
		  {
			text:'条件2：纯文本编辑器+ChatGPT',
			path:'studyNo_2',
			completed:true,
		  },
		  {
			text:'条件3：智能教案生成',
			path:'studyNo_3',
			completed:true,
		  },
		  {
			text:'条件4：智能教案生成+教案AI助手',
			path:'studyNo_4',
			completed:true,
		  }],// 原始按钮数组  
	      shuffledButtons: [], // 打乱后的按钮数组  
		  isButtonHidden:false,
		  matchTheme:[],
		  user_name:'',
		  orders:[],
		  id:0,
		  orderli:[{
			order:[1,2,3,4],
		  },{
			order:[2,3,4,1],
		  },
		{
			order:[3,4,1,2],
		},{
			order:[4,1,2,3],
		}],
		  
	    };  
	  },  
	 mounted() {
	 	//在该mounted中获取教师数据库中是否已经经历了shuffleButtons
		 
		//1-先获取当前教师的名字
		this.user_name = sessionStorage.getItem('user_name');
		console.log('我在这里：'+this.user_name);
		
		
		//2-根据当前教师的userName获取是否已经经历了shuffleButtons，是的话，isButtonHidden=true， study1 study2 study3 study4为数据库来的数据
		//获取实验顺序
				getstudyorder(this.user_name).then(response =>{
					console.log(response.data)
					if(response.data.length==0){
						//表明没有进行洗牌
						this.isButtonHidden=false;
					}else{
						//表明洗牌过一次，不用再洗牌一篇
						this.isButtonHidden=true;
						const order=response.data;
						this.radio=order[0].Subject;
						
						//它根据洗牌过后科目的选择相应的科目
				for(var i=0;i<this.subjects.length;i++){
			  if(this.subjects[i].text===this.radio){
				  //this.matchTheme=this.subjects[i].theme;
				  this.$set(this,'matchTheme',this.subjects[i].theme);
				  //console.log(this.matchTheme);
				  break;
			  }
		  }
						//console.log('从数据库取得了：'+this.radio);
                        this.shuffledButtons.push(this.buttons[order[0].Order1-1]);
						this.shuffledButtons.push(this.buttons[order[0].Order2-1]);
						this.shuffledButtons.push(this.buttons[order[0].Order3-1]);
						this.shuffledButtons.push(this.buttons[order[0].Order4-1]);
					}
				})
				.catch(error => {
					console.error('Error:', error);
				});
				
		//study1C study2C study3C study4C 按钮disable 若为1，则true，0为false
		// 取实验结果
		getstudyorderc(this.user_name).then(response =>{
					console.log(response.data)
					const orderc=response.data;
					if(orderc[0].Order1C==0){
						//表明未完成实验
						this.shuffledButtons[0].completed=true;
					}else{

						this.$set(this.shuffledButtons[0],'completed',false);
					}
					if(orderc[0].Order2C==0){
						//表明未完成实验
						this.shuffledButtons[1].completed=true;
					}else{
	
						//this.$set响应式
						this.$set(this.shuffledButtons[1],'completed',false);
					}
					if(orderc[0].Order3C==0){
						//表明未完成实验
						this.shuffledButtons[2].completed=true;
					}else{
			
						this.$set(this.shuffledButtons[2],'completed',false);
					}
					if(orderc[0].Order4C==0){
						//表明未完成实验
						this.shuffledButtons[3].completed=true;
					}else{
				
						this.$set(this.shuffledButtons[3],'completed',false);
					}
				})
				.catch(error => {
					console.error('Error:', error);
				});

	 },
	  methods: {  


	   async shuffleButtonsa() {  
			        console.log('new radio:'+this.radio);
					try {
						const response = await getsubjectnum(this.radio);
						console.log('response data:' + response.data);
						this.id = response.data;
							console.log('new id:' + this.id);
							} catch (error) {
								console.error('Error:', error);
								}

				console.log('id:'+this.id);

		  this.isButtonHidden=true;
		  //1-先获取用户的id值
		  // 测试 获取实验顺序

		
				let orderl=this.id%4;
				this.orders=[...this.orderli[orderl].order];
				console.log("this.orders"+this.orders);
				this.shuffledButtons.push(this.buttons[this.orders[0]-1]);
				console.log(this.buttons[this.orders[0]-1]);
				this.shuffledButtons.push(this.buttons[this.orders[1]-1]);
				this.shuffledButtons.push(this.buttons[this.orders[2]-1]);
				this.shuffledButtons.push(this.buttons[this.orders[3]-1]);
				console.log('this.shuffledButtons:'+this.shuffledButtons[0]);

		  
		  let sub=this.radio;
		  console.log('radio:'+sub);
		  for(var i=0;i<this.subjects.length;i++){
			  if(this.subjects[i].text===this.radio){
				  //this.matchTheme=this.subjects[i].theme;
				  this.$set(this,'matchTheme',this.subjects[i].theme);
				  console.log(this.matchTheme);
		
				  break;
			  }
		  }

		  //数据库：把实验顺序存入教师档案中
		  // 测试 插入顺序
				insertstudyorder(this.user_name,sub,this.orders[0],this.orders[1],this.orders[2],this.orders[3]).then(response =>{
					this.$message({
						message: '成功！',
						type: 'success'
						});
				})
				.catch(error => {
					console.error('Error:', error);
				});
				
		  
	    },
		gotoStudy(path,index){
			//把教案主题列表、条件顺序、跳转路径放进去
			sessionStorage.setItem('matchTheme', JSON.stringify(this.matchTheme));
			sessionStorage.setItem('index',index.toString());
			sessionStorage.setItem('path',path);
			sessionStorage.setItem('radio',this.radio);


			// let index1 = sessionStorage.getItem('index');
            // let index2 = parseInt(index1);
			// console.log('index2: session:'+index2);
			// let retrievedList = JSON.parse(sessionStorage.getItem('matchTheme'));
            // console.log('relist session:'+ retrievedList[index]); // [1, 2, 3, 'four', 'five']
			// let path1 = sessionStorage.getItem('path');
			// console.log('path1 session:'+path1); // [1, 2, 3, 'four', 'five']
			// let radio1 = sessionStorage.getItem('radio');
			// console.log('radio1 session:'+radio1); // [1, 2, 3, 'four', 'five']

			const m=this.matchTheme[index];
			
			const r=this.radio;
			if(path=='studyNo_1'||path=='studyNo_2'){
				this.$router.push({name:path,
								    params:{
								    radio:r,
									matchTheme:m,
									order:index,
									}
				});
			}else{
				this.$router.push({name:'Inputinfo',
								    params:{
									path:path,
									radio:r,
									matchTheme:m,
									order:index,
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
		  margin-right: 20px;
	  }
	 

</style>