//该js文件为wangedito新菜单的函数构造 --ai编辑功能
import { IButtonMenu, IDomEditor } from '@wangeditor/editor'


export default class MyButtonMenu {                       // JS 语法

    constructor() {
       this.title = 'AI编辑' // 自定义菜单标题
       this.tag = 'button'
    }

    // 获取菜单执行时的 value ，用不到则返回空 字符串或 false
   getValue(editor) {                              // JS 语法
        return editor.getSelectionText()
    }

    // 菜单是否需要激活（如选中加粗文本，“加粗”菜单会激活），用不到则返回 false
   // TS 语法
     isActive(editor) {                    // JS 语法
        return false
    }

    // 菜单是否需要禁用（如选中 H1 ，“引用”菜单被禁用），用不到则返回 false
  // TS 语法
    isDisabled(editor) {                     // JS 语法
        return false
    }

    // 点击菜单时触发的函数
 // TS 语法
   exec(editor, value) {
	   // JS 语法
        if (this.isDisabled(editor)) return
        editor.insertText(value) // value 即 this.value(editor) 的返回值
    }

}
