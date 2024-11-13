<template>
<el-container style="">
  <el-header>
    <el-button type="primary" icon="el-icon-folder-add" @click="newspace()">新建</el-button>
  </el-header>
  <el-main style="background-color: rgb(255, 247, 247);" >
	<h4>历史教案</h4>
	<el-table :data="tableData"  align="center" style="width: 100%">
      <el-table-column prop="LessonName" label="教案名称" width="380" ></el-table-column>
      <el-table-column prop="UserName" label="作者" width="380" > </el-table-column>
      <el-table-column prop="time" label="操作" width="380">
		<template slot-scope="scope">
        <el-button @click="handleSeleUserId(scope.row)" type="text" size="big">编辑</el-button>
		<el-button @click="delspace(scope.row)" type="text" size="big">删除</el-button>
		</template>
	 </el-table-column>
    </el-table>

  </el-main>
</el-container>
</template>

<script>
import {getuserLessondata,delLessondata,getLessondata} from '../api/api.js'
	export default {
		data() {
			return {
				tableData: [],
				un:"",
			}
		},
		created() {
			this.fetchUserData();
		},
		methods: {
			// 新建教案 -main.vue
			newspace() {
				// this.$router.push({ name: 'SmartEdu',params:{lessonName:'lessonInfo'} })
				this.$router.push({ name: 'Inputinfo',params:{lessonName:'lessonInfo'} })
			},
			// 删除教案 
			delspace(row) {
				delLessondata(row.id).then(response =>{
					this.fetchUserData();
				})
				.catch(error => {
					console.error('Error:', error);
				});
				
			},
			fetchUserData() {
				const user_name = sessionStorage.getItem('user_name');
				this.un=user_name;
				console.log(user_name);
				// const user_name = localStorage.getItem('user_name');
				getuserLessondata(user_name).then(response =>{
					this.tableData = response.data;
					console.log(response.data);
				})
				.catch(error => {
					console.error('Error:', error);
				});
				
			},
			//编辑教案 - lessontemplate.vue
			handleSeleUserId(row) {
				// var lname='';
				// getLessondata(row.id).then(response =>{
				// 	console.log(response.data);
				// 	this.tableData = response.data;
				// 	 lname = this.tableData[0].LessonName;
				// 	console.log(lname);
				// })
				// .catch(error => {
				// console.error('Error:', error);
				// });
				//window.location.href = `http://127.0.0.1:9001/p/我上学了`;
				
				this.$router.push({name:'lessontemplate',
								    params:{
									id:row.id,
									}
				});
			}
		}
	}
</script>


<style>
  .text {
    font-size: 14px;
  }

  .item {
    margin-bottom: 18px;
  }

  .clearfix:before,
  .clearfix:after {
    display: table;
    content: "";
  }
  .clearfix:after {
    clear: both
  }

  .box-card {
    width: 480px;
  }
 
</style>