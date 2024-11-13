import Vue from 'vue'
import App from './App.vue'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import router from './router/index.js'
import './css/wangEditor.css'
import 'animate.css';
import VueKatex from 'vue-katex';
import 'katex/dist/katex.min.css';

Vue.config.productionTip = false
Vue.use(ElementUI);
Vue.use(ElementUI);
//因为我生成的是以 $ 开头结束的，所以在里面定义了界定符；注意一点：如果不在里面定义好，可能不会渲染，因为我就是这样。
Vue.use(VueKatex, {
  globalOptions: {
         //定义好界定符，好让它能够找到渲染的latex公式块
	  delimiters: [
	                {left: '$$', right: '$$', display: true},
	                {left: '$', right: '$', display: false},
	                {left: '\\(', right: '\\)', display: true},
	                {left: '\\[', right: '\\]', display: true}
	            ],
    //... Define globally applied KaTeX options here
  }
});




new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
