<template>
<el-container style="">
  <el-header>
    <el-button type="primary" icon="el-icon-folder-add" @click="newspace()">新建</el-button>
	<!-- <el-button type="primary" icon="el-icon-delete-solid" @click="delspace()">删除</el-button> -->
  </el-header>
  <el-main style="background-color: rgb(255, 247, 247);" >
	<h4>历史教案</h4>
    <!-- <div>
		<el-card class="box-card">
		<div slot="header" class="clearfix">
			<span>教案名称1</span>
			<el-button style="float: right; padding: 3px 0" type="text"></el-button>
		</div>
		<div v-for="item in items" :key="item.id" class="text item">
			{{item.name }}
		</div>
		</el-card>
    </div>
	<div>
		<el-card class="box-card">
		<div slot="header" class="clearfix">
			<span>教案名称2</span>
			<el-button style="float: right; padding: 3px 0" type="text"></el-button>
		</div>
		<div v-for="item in items" :key="item.id" class="text item">
			{{item.name }}
		</div>
		</el-card>
    </div>
	<div>
		<el-card class="box-card">
		<div slot="header" class="clearfix">
			<span>教案名称3</span>
			<el-button style="float: right; padding: 3px 0" type="text"></el-button>
		</div>
		<div v-for="item in items" :key="item.id" class="text item">
			{{item.name }}
		</div>
		</el-card>
    </div>
	<div>
		<el-card class="box-card">
		<div slot="header" class="clearfix">
			<span>教案名称4</span>
			<el-button style="float: right; padding: 3px 0" type="text"></el-button>
		</div>
		<div v-for="item in items" :key="item.id" class="text item">
			{{item.name }}
		</div>
		</el-card>
    </div>
	<div>
		<el-card class="box-card">
		<div slot="header" class="clearfix">
			<span>教案名称5</span>
			<el-button style="float: right; padding: 3px 0" type="text"></el-button>
		</div>
		<div v-for="item in items" :key="item.id" class="text item">
			{{item.name }}
		</div>
		</el-card>
    </div> -->
	<el-table :data="tableData"  align="center" style="width: 100%"  >
      <el-table-column prop="LessonName" label="教案名称" width="380" ></el-table-column>
      <el-table-column prop="UserName" label="作者" width="380"> </el-table-column>
      <el-table-column prop="time" label="操作" width="380">
		<template slot-scope="scope">
        <el-button @click="handleSeleUserId(scope.row)" type="text" size="big">编辑</el-button>
		<el-button @click="delspace(scope.row)" type="text" size="big">删除</el-button>
		</template>
	 </el-table-column>
	 <!-- <el-table-column prop="id" label="" ></el-table-column> -->
    </el-table>

  </el-main>
</el-container>
</template>

<script>
import {getuserLessondata,delLessondata} from '../api/api.js'
	export default {
		data() {
			return {
				tableData: []
			}
		},
		created() {
			this.fetchUserData();
		},
		methods: {
			newspace() {
				this.$router.push('/SmartEdu');
			},
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
				// const user_name = localStorage.getItem('user_name');
				getuserLessondata(user_name).then(response =>{
					this.tableData = response.data;
					console.log(response.data);
				})
				.catch(error => {
					console.error('Error:', error);
				});
				
			},
			handleSeleUserId(row) {
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