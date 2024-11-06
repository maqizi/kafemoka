<template>
	<div class="center">
		<h1>Welcome to SmartEdu</h1>
		<div class="logon">
			<div :class="overlaylong">
				<div class="overlaylong-Signin" v-if="disfiex == 0">
					<h2 class="overlaylongH2">Sign in</h2>
					<input type="text" placeholder="user" v-model="SignInUser.user">
					<input type="text" placeholder="password" v-model="SignInUser.password">
					<h3>Forgot your password?</h3>
					<button class="inupbutton" type="submit" @click="userSignin()">Sign in</button>
				</div>
				<div class="overlaylong-Signup" v-if="disfiex == 1">
					<h2 class="overlaylongH2">Registered Account</h2>
					<input type="text" placeholder="user" v-model="SignUpUser.user">
					<input type="text" placeholder="password" v-model="SignUpUser.password">
					<button class="inupbutton" type="submit" @click="userSignup()">Sign up</button>
				</div>
 
			</div>
			<div :class="overlaytitle">
				<div class="overlaytitle-Signin" v-if="disfiex == 0">
					<h2 class="overlaytitleH2">Hello,Friend!</h2>
					<p class="overlaytitleP">
						Enter your personal details and start journey with us
					</p>
					<div class="buttongohs" @click="Signin">Sign up</div>
				</div>
				<div class="overlaytitle-Signup" v-if="disfiex == 1">
					<h2 class="overlaytitleH2">Welcome Back!</h2>
					<p class="overlaytitleP">To keep connected with us please login with your personal info</p>
					<div class="buttongohs" @click="Signup">Sign in</div>
				</div>
			</div>
		</div>
 
	</div>
</template>

<style scoped>
	.center {
		width: 100%;
		height: 100%;
		background-image: url(../assets/Maldives.png);
		/* background-color: #acd1fd; */
		background-size: 100% 100%;
		background-repeat: no-repeat;
		display: flex;
		align-items: center;
		justify-content: center;
		flex-direction: column;
	}
 
	h1 {
		font-size: 30px;
		color: black;
	}
 
	.logon {
		background-color: #fff;
		border-radius: 10px;
		box-shadow: 0 14px 28px rgba(0, 0, 0, 0.25), 0 10px 10px rgba(0, 0, 0, 0.22);
		/* position: relative;
		overflow: hidden; */
		width: 768px;
		max-width: 100%;
		min-height: 480px;
		margin-top: 20px;
		display: flex;
		background: -webkit-linear-gradient(right, #4284db, #29eac4);
	}
 
	.overlaylong {
		border-radius: 10px 0 0 10px;
		width: 50%;
		height: 100%;
		background-color: #fff;
		display: flex;
		align-items: center;
		justify-content: center;
	}
 
	.overlaylongleft {
		border-radius: 0px 10px 10px 0px;
		width: 50%;
		height: 100%;
		background-color: #fff;
		transform: translateX(100%);
		transition: transform 0.6s ease-in-out;
		display: flex;
		align-items: center;
		justify-content: center;
	}
 
	.overlaylongright {
		border-radius: 10px 0 0 10px;
		width: 50%;
		height: 100%;
		background-color: #fff;
		transform: translateX(0%);
		transition: transform 0.6s ease-in-out;
		display: flex;
		align-items: center;
		justify-content: center;
	}
 
	.overlaytitle {
		border-radius: 0px 10px 10px 0px;
		width: 50%;
		height: 100%;
		background-color: rgba(0, 0, 0, 0);
		display: flex;
		align-items: center;
		justify-content: center;
	}
 
 
	.overlaytitleH2 {
		font-size: 30px;
		color: #fff;
		margin-top: 20px;
	}
 
	.overlaytitleP {
		font-size: 15px;
		color: #fff;
		margin-top: 20px;
	}
 
	.overlaytitleleft {
		border-radius: 0px 10px 10px 0px;
		width: 50%;
		height: 100%;
		background-color: rgba(0, 0, 0, 0);
		display: flex;
		align-items: center;
		justify-content: center;
		transform: translateX(0%);
		transition: transform 0.6s ease-in-out;
	}
 
	.overlaytitleright {
		border-radius: 0px 10px 10px 0px;
		width: 50%;
		height: 100%;
		background-color: rgba(0, 0, 0, 0);
		display: flex;
		align-items: center;
		justify-content: center;
		transform: translateX(-100%);
		transition: transform 0.6s ease-in-out;
	}
 
	.overlaytitle-Signin {
		display: flex;
		align-items: center;
		justify-content: center;
		flex-direction: column;
	}
 
	.overlaytitle-Signup {
		display: flex;
		align-items: center;
		justify-content: center;
		flex-direction: column;
	}
 
	.buttongohs {
		width: 180px;
		height: 40px;
		border-radius: 50px;
		border: 1px solid #fff;
		color: #fff;
		font-size: 15px;
		text-align: center;
		line-height: 40px;
		margin-top: 40px;
	}
 
	.overlaylongH2 {
		font-size: 25px;
		color: black;
		/* width: 250px; */
	}
 
	.overlaylong-Signin {
		display: flex;
		align-items: center;
		justify-content: center;
		flex-direction: column;
	}
 
	.overlaylong-Signup {
		display: flex;
		align-items: center;
		justify-content: center;
		flex-direction: column;
	}
 
	input {
		background-color: #eee;
		border: none;
		padding: 12px 15px;
		margin: 10px 0;
		width: 240px;
	}
	h3{
		font-size: 10px;
		margin-top: 10px;
		cursor: pointer;
	}
	.inupbutton{
		background-color: #29eac4;
		border: none;
		width: 180px;
		height: 40px;
		border-radius: 50px;
		font-size: 15px;
		color: #fff;	
		text-align: center;
		line-height: 40px;
		margin-top: 30px;
	}
</style>

<script>
import {registerUser, loginUser} from '../api/api.js'
	export default {
		data() {
			return {
				overlaylong: 'overlaylong',
				overlaytitle: 'overlaytitle',
				disfiex: 0,
				// user data in the form
				SignUpUser: {
					"user": "",
					"password": "",
      			},
				SignInUser: {
					"user": "",
					"password": "",
      			}
			}
		},
		methods: {
			Signin() {
				this.overlaylong = "overlaylongleft"
				this.overlaytitle = "overlaytitleright"
				setTimeout(() => {
					this.disfiex = 1
				}, 200)
			},
			Signup() {
				this.overlaylong = "overlaylongright"
				this.overlaytitle = "overlaytitleleft"
 
				setTimeout(() => {
					this.disfiex = 0
				}, 200)
			},
			userSignup(){
				registerUser(this.SignUpUser.user, this.SignUpUser.password).then(response => {
					// console.log(response.data.status);
					if(response.data.status == true){
						// 注册成功，显示成功框
						this.$message({
								message: '注册成功',
								type: 'success'
								});
					}
					else
					{
						this.$message.error('注册失败！');
					}
				})
				.catch(error => {
					this.$message.error('注册失败！！');
					});
			},
			userSignin(){
				loginUser(this.SignInUser.user, this.SignInUser.password).then(response => {
					if(response.status == 200){
						// 注册成功，显示成功框
						this.$message({
						message: '登入成功！',
						type: 'success'
						});
						// console.log(response.data)
						sessionStorage.setItem('is_login', 'true')
						sessionStorage.setItem('token', response.data.token)
						sessionStorage.setItem('user_id', response.data.user_id)
						sessionStorage.setItem('user_name', response.data.user_name)
						// localStorage.setItem('is_login', 'true')
						// localStorage.setItem('token', response.data.token)
						// localStorage.setItem('user_id', response.data.user_id)
						// localStorage.setItem('user_name', response.data.user_name)
						this.$router.push('/Workspace');
					}
					else
					{
						this.$message.error('登入失败！');
					}
				})
				.catch(error => {
					this.$message.error('登入失败！!');
					});
				
			},
			
			
		}
	}
</script>