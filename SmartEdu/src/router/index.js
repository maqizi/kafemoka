import Vue from 'vue'   //引入Vue
import Router  from 'vue-router'  //引入vue-router
import SmartEdu from '../components/main.vue'  
import SignIn from '../components/SignIn.vue'
import Workspace from '../components/workspace.vue'
import LessonEditByAI from '../components/LessonEditByAI.vue'
import lessontemplate from '../components/lessontemplate.vue'
import Inputinfo from '../components/inputInfo.vue'
import lessonGen from '../components/lessonGen.vue'

// studySum整体进入
import studySum from '../components/studySum.vue'
import studyNo_1 from '../components/studyNo_1.vue'
import studyNo_2 from '../components/studyNo_2.vue'
import studyNo_3 from '../components/studyNo_3.vue'
import studyNo_4 from '../components/studyNo_4.vue'


Vue.use(Router )  //Vue全局使用Router
 
  const routes = [
	{
	  path:'/',
	  name:'SignIn',
	  component: SignIn,
	},
	{
		path:'/studySum',
		name:'studySum',
		component: studySum,
	},
	{
		path:'/studyNo_1',
		name:'studyNo_1',
		component: studyNo_1,
	},
	{
		path:'/studyNo_2',
		name:'studyNo_2',
		component: studyNo_2,
	},
	{
		path:'/studyNo_3',
		name:'studyNo_3',
		component: studyNo_3,
	},
	{
		path:'/studyNo_4',
		name:'studyNo_4',
		component: studyNo_4,
	},

    {
      path:"/SignIn",
      component:SignIn
    },
    {
      path:"/SmartEdu",
	  name:'SmartEdu',
      component:SmartEdu
    },
    {
      path:"/Workspace",
      component:Workspace
    },
    {
      path:"/LessonEditByAI",
	  name:'LessonEditByAI',
      component:LessonEditByAI
    },
    {
      path:"/lessontemplate",
      name:'lessontemplate',
      component:lessontemplate
    },
	{
	  path:"/Inputinfo",
	  name:'Inputinfo',
	  component:Inputinfo
	},
	{
	  path:"/lessonGen",
	  name:'lessonGen',
	  component:lessonGen
	},
    
  ]
  const router = new Router ({
    mode: 'history',
    routes,
    
  });

  router.beforeEach((to, from, next)=>{
    // const isLogin = localStorage.getItem('is_login') == 'true';
    const isLogin = sessionStorage.getItem('is_login') == 'true';
    
    if( isLogin ){
      if( to.path !== '/SignIn' )
        next();
      else
        next('/')
    } else {
      if( to.path !== '/SignIn')
        next('/SignIn');
      else
        next();
    }
  });

export default router;

   


