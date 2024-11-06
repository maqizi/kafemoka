import Vue from 'vue'   //引入Vue
import Router  from 'vue-router'  //引入vue-router
import SmartEdu from '../components/main.vue'  
import SignIn from '../components/SignIn.vue'
import Etherpad from '../components/etherpad.vue'
import Workspace from '../components/workspace.vue'
import LessonEditByAI from '../components/LessonEditByAI.vue'
import lessontemplate from '../components/lessontemplate.vue'
Vue.use(Router )  //Vue全局使用Router
 
  const routes = [
    {
      path:'/',
      name:'SignIn',
      component: SignIn,
    },
    {
      path:"/SignIn",
      component:SignIn
    },
    {
      path:"/SmartEdu",
      component:SmartEdu
    },
    {
      path:"/Etherpad",
      component:Etherpad
    },
    {
      path:"/Workspace",
      component:Workspace
    },
    {
      path:"/LessonEditByAI",
      component:LessonEditByAI
    },
    {
      path:"/lessontemplate",
      name:'lessontemplate',
      component:lessontemplate
    },
    
  ]
  const router = new Router ({
    mode: 'history',
    routes,
    
  });

  router.beforeEach((to, from, next)=>{
    // const isLogin = localStorage.getItem('is_login') == 'true';
    const isLogin = sessionStorage.getItem('is_login') == 'true';
    
    // if( isLogin ){
    //   if( to.path !== '/SignIn' )
    //     next();
    //   else
    //     next('/')
    // } else {
    //   if( to.path !== '/SignIn')
    //     next('/SignIn');
    //   else
    //     next();
    // }
  });

export default router;

   


