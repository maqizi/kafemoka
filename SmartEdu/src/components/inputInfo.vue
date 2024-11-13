<template >

    <div class="SetBackground"> 
	
        <el-form ref="form" :model="form" label-width="80px" @submit.native.prevent >
            
            <div style="padding-top: 0.725rem;">
                <!-- <div class="title" >
                    <img :src="Logo" alt="Image" size="32" style="width:100px " >
                    <span style="font-weight: bold;font-size: 25px;">暨南大学广东智慧教育研究院 教案生成</span>
                </div> -->
				<div class="hayabox">
				<el-avatar :size="50" :src="img_AI" class="animate__animated animate__pulse"></el-avatar>
				<!-- <span class="animate__animated animate__fadeInDown haya"> -->
				<span class="haya">
				    你好！我是你的教案生成助手。让我们开始生成属于你的教案吧！<span class="animate__animated animate__flash animate__infinite">_</span>
				</span>
				</div>
				<!-- <div class="hayabox">请注意，您在此实验条件中的教案主题为：<<{{matchT}}>>,请在以下课程信息中输入教案主题。</div>
				<div class="hayabox">请点击开始按钮，开始点击之后，开始计时。</div>
				<div class="hayabox">
				<el-button @click="startTimer">开始</el-button>
				<el-button>经历时间：{{ elapsedTime }}</el-button>
				</div> -->
                <div class="backgroundPlate">
               
                <div class="block">
                  课程信息：
                        <el-cascader v-model="basic_info" :options="basic_options" filterable >
                        </el-cascader>
                </div>
                <div class="block">
                    <div class="JayChou">
						授课模式：
						    <el-select v-model="select_value" filterable placeholder="请选择" @change="display_selected">
						    <el-option v-for="item in select_options" :key="item.value" :label="item.label" :value="item.value" >
						    </el-option>
						    </el-select>
                        第
                        <el-input-number v-model="num" controls-position="right" @change="handleChange" :min="1" :max="10" ></el-input-number>
                       课时
                    </div>
                </div>                
                <div class="block">
					<span style="float: left;margin-top: 0.55rem;">教学结构：</span>    
					<el-checkbox-group v-model="checkboxValues">
						<el-checkbox label="教学内容分析"  border> 教学内容分析</el-checkbox>
					    <el-checkbox label="学情分析" border></el-checkbox>
                        <el-checkbox label="教学目标"  border >教学目标(必选)</el-checkbox>
                        <el-checkbox label="教学重难点"  border @click="Vision"></el-checkbox>
					    <el-checkbox label="教学过程" border >教学过程(必选)</el-checkbox>
					    <el-checkbox label="学习评价"  border></el-checkbox>
					    <el-checkbox label="课后作业" border></el-checkbox>
						<el-button icon="el-icon-delete" @click="ClearSelection" circle size="mini" style="margin-left: 0.4125rem;"></el-button>      
					</el-checkbox-group>         
				</div>
				<div class="block">
					<span style="float: left;margin-top: 0.55rem;">教学模式：</span>    
					<!-- 教学模式 -start -->
					<div class="container container-with-shadow" >
					    <el-container style="height: 400px  ;">

					    <el-container>
					    <!-- 左侧菜单栏 -->
					    <el-aside width="200px" style="overflow-y:auto;height: 100%;">
					        <el-menu default-active="1" @select="handleMenuSelect" style="height: 100%;">
                            <el-menu-item index="1">自定义教学</el-menu-item>
					        <el-menu-item index="2">探究式教学</el-menu-item>
					        <el-menu-item index="3">讲授式教学</el-menu-item>
					        <el-menu-item index="4">协作式教学</el-menu-item>
					        <el-menu-item index="5">讲座式教学</el-menu-item>
					        <el-menu-item index="6">情景式教学</el-menu-item>
					        <el-menu-item index="7">研究式教学</el-menu-item> 
                            <el-menu-item index="8">语文阅读课教学</el-menu-item>
					        <el-menu-item index="9">古诗阅读教学</el-menu-item> 
					        </el-menu>
					    </el-aside>
					    <!-- 右侧内容显示区域 -->
					    <el-main class="content-container" style="overflow-y: auto;height: 100%;">
                            <div v-if="currentTab === '1'">
					            <div>
					                <span style="font-weight: bold;display: inline-block ;height: fit-content; margin-bottom :20px;text-align: center; ">模式简介
					                </span><br>
					                <span style="text-align: center;">您可以根据自身需要自定义本节课的教学环节。</span>
					            </div>
					
					
					
					            <div style="margin-top: 20px ">
					                <span style="font-weight: bold;display: inline-block ;height: fit-content; margin-bottom :20px; ">教学环节
					                </span><br>
					                <div class="draggable-container">
					                    
					                    <draggable  :list="list" :disabled="!enabled" class="list-group" ghost-class="ghost"
					                        :move="checkMove" @start="dragging = true" @end="dragging = false">
					
					                        <div v-for="(element,index) in list " :key="element.id" class="user-defined">
					        
					                            <span>{{ indexToChar(index) }}、</span>
					                            <el-input type="text"  class="list-group-item"  v-model="element.name"    placeholder="请输入内容">
					                            </el-input>
					                            
					                            <!-- <el-input type="text"  class="list-group-item"  v-model="item.content"    placeholder="请输入内容">
					                            </el-input> -->
					
					                            <el-button     @click="handleRemove(index)"  >
					                                删除
					                                </el-button>  
					                        </div>
					                        <!-- <el-input type="text"  class="list-group-item" v-for="element in list" :key="element.id" v-model="element.name"  :value="element.name || ''"  placeholder="请输入内容">
					                            </el-input> -->
					                        </draggable>
					                    </div>
					                    <el-button    type="primary"  @click="handleAdd()"  >
					                                添加
					                                </el-button>  
					                </div>
					        </div>
					        <div  v-else-if="currentTab === '2'" style="height: 100%;">
					            <div>
					                <span style="font-weight: bold;display: inline-block ;height: fit-content; margin-bottom :20px; ">模式简介
					                </span><br>
					                <span style="margin-top: 20px">探究式教学以问题解决为中心的，注重学生的独立活动，注重体验式教学，着眼于学生的思维能力的培养。</span>
					            </div>
					            <div style="margin-top: 20px">
					                <span style="font-weight: bold;display: inline-block ;height: fit-content; margin-bottom :20px; ">教学环节
					                </span><br>
					                <span style="display: inline-block; text-align: left; margin-left: 60px;width: 100%;"  >一、情境创设，课程导入</span><br>
					                <span style="display: inline-block; text-align: left; margin-left: 60px;width: 100%;"  >二、分析问题，明确目标</span><br>
					                <span style="display: inline-block; text-align: left; margin-left: 60px;width: 100%;"  >三、动手实践，探究新知</span><br>
					                <span style="display: inline-block; text-align: left; margin-left: 60px;width: 100%;"  >四、课堂总结，建构概念</span><br>
					                <span style="display: inline-block; text-align: left; margin-left: 60px;width: 100%;"  >五、知识巩固，迁移应用</span><br>
					            </div>
					        </div>
					        <div v-else-if="currentTab === '3'">
					            <div>
					                <span style="font-weight: bold;display: inline-block ;height: fit-content; margin-bottom :20px; ">模式简介
					                </span><br>
					                <div style="text-align: left">该模式以传授系统知识、培养基本技能为目标。其着眼点在于充分挖掘人的记忆力、推理能力与间接经验在掌握知识方面的作用，使学生比较快速有效地掌握更多的信息量。</div>
					            </div>
					            <div style="margin-top: 20px">
					                <span style="font-weight: bold;display: inline-block ;height: fit-content; margin-bottom :20px; ">教学环节
					                </span><br>
					
					                <span style="display: inline-block; text-align: left; margin-left: 60px;width: 100%;"  >一、导入新课</span><br>
					                <span style="display: inline-block; text-align: left; margin-left: 60px;width: 100%;"  >二、检查复习</span><br>
					                <span style="display: inline-block; text-align: left; margin-left: 60px;width: 100%;"  >三、讲授新课</span><br>
					                <span style="display: inline-block; text-align: left; margin-left: 60px;width: 100%;"  >四、巩固新课</span><br>
					                <span style="display: inline-block; text-align: left; margin-left: 60px;width: 100%;"  >五、课堂总结</span><br>
					                <span style="display: inline-block; text-align: left; margin-left: 60px;width: 100%;"  >六、布置作业</span><br>
					            </div>
					        </div>
					        <div v-else-if="currentTab === '4'">
					            <div>
					                <span style="font-weight: bold;display: inline-block ;height: fit-content; margin-bottom :20px; ">模式简介
					                </span><br>
					                <div style="text-align: left">协作式教学模式是一种强调学生互相合作、参与和共同构建知识的教学方法。它强调学生在教学过程中的积极参与和合作，促进他们的自主学习和批判性思维能力的培养。</div>
					            </div>
					            <div style="margin-top: 20px">
					                <span style="font-weight: bold;display: inline-block ;height: fit-content; margin-bottom :20px; ">教学环节
					                </span><br>
					
					                <span style="display: inline-block; text-align: left; margin-left: 60px;width: 100%;"  >一、课程导入，明确主题</span><br>
					                <span style="display: inline-block; text-align: left; margin-left: 60px;width: 100%;"  >二、围绕主题，明确问题</span><br>
					                <span style="display: inline-block; text-align: left; margin-left: 60px;width: 100%;"  >三、小组协作，解决问题</span><br>
					                <span style="display: inline-block; text-align: left; margin-left: 60px;width: 100%;"  >四、成果展示，交流汇报</span><br>
					                <span style="display: inline-block; text-align: left; margin-left: 60px;width: 100%;"  >五、总结评价，优化方案</span><br>
					            </div>
					        </div> 
					        
					
					        <div v-else-if="currentTab === '5'">
					            <div>
					                <span style="font-weight: bold;display: inline-block ;height: fit-content; margin-bottom :20px; ">模式简介
					                </span><br>
					                <div style="text-align: left">对于相对独立或者前沿的教学内容，通过讲座的形式，教师或学生做主题发言，然后集体讨论探讨，让学生通过自学解决自己所能解决的问题，而把教师的主要精力用于指导学生的学习方法，解决教学中的重点、难点，既能加深对学习主题的理解，又扩充了学生学习的知识领域。</div>
					            </div>
					            <div style="margin-top: 20px">
					                <span style="font-weight: bold;display: inline-block ;height: fit-content; margin-bottom :20px; ">教学环节
					                </span><br>
					
					                <span style="display: inline-block; text-align: left; margin-left: 60px;width: 100%;"  >一、教师分组，确定讲座主题</span><br>
					                <span style="display: inline-block; text-align: left; margin-left: 60px;width: 100%;"  >二、小组分工，协作准备</span><br>
					                <span style="display: inline-block; text-align: left; margin-left: 60px;width: 100%;"  >三、举行专题讲座</span><br>
					                <span style="display: inline-block; text-align: left; margin-left: 60px;width: 100%;"  >四、提问答疑</span><br>
					                <span style="display: inline-block; text-align: left; margin-left: 60px;width: 100%;"  >五、提交讲稿、报告</span><br>
					            </div>
					        
					        </div>
					        <div v-else-if="currentTab === '6'">
					            <div>
					                <span style="font-weight: bold;display: inline-block ;height: fit-content; margin-bottom :20px; ">模式简介
					                </span><br>
					                <div style="text-align: left">应用情境教学法，设置与教学内容相关的情境，将教学内容理论知识和实践技能结合起来，模拟真实场景，通过学生间相互合作和协调，使学生真正成为课堂教学中的主体和自我发展的主体，从而科学有效地解决综合性实验教学中的问题，为理论教学和实践教学的结合提供良好的平台。</div>
					            </div>
					            <div style="margin-top: 20px">
					                <span style="font-weight: bold;display: inline-block ;height: fit-content; margin-bottom :20px; ">教学环节
					                </span><br>
					
					                <span style="display: inline-block; text-align: left; margin-left: 60px;width: 100%;" >一、设置问题情境，确立实验项目</span><br>
					                <span style="display: inline-block; text-align: left; margin-left: 60px;width: 100%;" >二、小组分配</span><br>
					                <span style="display: inline-block; text-align: left; margin-left: 60px;width: 100%;" >三、查找资料</span><br>
					                <span style="display: inline-block; text-align: left; margin-left: 60px;width: 100%;" >四、设计实验方案</span><br>
					                <span style="display: inline-block; text-align: left; margin-left: 60px;width: 100%;" >五、体验模拟</span><br>
					                <span style="display: inline-block; text-align: left; margin-left: 60px;width: 100%;" >六、教师点评</span><br>
					                <span style="display: inline-block; text-align: left; margin-left: 60px;width: 100%;" >七、提交体验报告</span><br>
					
					            </div>
					        
					        </div>
					
					        <div v-else-if="currentTab === '7'">
					            <div>
					                <span style="font-weight: bold;display: inline-block ;height: fit-content; margin-bottom :20px; ">模式简介
					                </span>
					                <div style="text-align: left">在教学的过程中，教师把研究的项目及方向和教学课程相结合，在教师的指导下，通过阅读文献或课题研究，在学习中研究、在研究中学习，遇到了问题深入分析研究，用已有知识学习求解问题所需要的知识，使学习和研究成为一个互动的过程。在研讨中积累知识、培养能力和锻炼思维。</div>
					                <!-- <span style="display:inline-block ;width:100%;text-align: left">在教学的过程中，教师把研究的项目及方向和教学课程相结合，在教师的指导下，通过阅读文献或课题研究，在学习中研究、在研究中学习，遇到了问题深入分析研究，用已有知识学习求解问题所需要的知识，使学习和研究成为一个互动的过程。在研讨中积累知识、培养能力和锻炼思维。</span> -->
					            </div>
					            <div style="margin-top: 20px">
					                <span style="font-weight: bold;display: inline-block ;height: fit-content; margin-bottom :20px; ">教学环节
					                </span><br>
					
					                <span style="display: inline-block; text-align: left; margin-left: 60px;width: 100%;">一、教师提出课题</span><br>
					                <span style="display: inline-block; text-align: left; margin-left: 60px;width: 100%;">二、小组分工，协作准备</span><br>
					                <span style="display: inline-block; text-align: left; margin-left: 60px;width: 100%;">三、深入研究</span><br>
					                <span style="display: inline-block; text-align: left; margin-left: 60px;width: 100%;">四、集体研讨</span><br>
					                <span style="display: inline-block; text-align: left; margin-left: 60px;width: 100%;">五、完成报告</span><br>
					                <span style="display: inline-block; text-align: left; margin-left: 60px;width: 100%;">六、评价</span><br>
					            </div>
					        
					        </div>
                            <div v-else-if="currentTab === '8'">
					            <div>
					                <span style="font-weight: bold;display: inline-block ;height: fit-content; margin-bottom :20px; ">模式简介
					                </span>
					                <div style="text-align: left">语文阅读课教学模式旨在通过创设情境、课文品读、拓展阅读、知识应用和评价反馈等环节，培养学生的阅读能力、理解能力和写作能力。通过引发学生的兴趣，帮助他们深入理解课文内容，扩展知识面并将所学知识应用到写作中，该教学模式能够全面发展学生的语文素养。</div>
					                <!-- <span style="display:inline-block ;width:100%;text-align: left">在教学的过程中，教师把研究的项目及方向和教学课程相结合，在教师的指导下，通过阅读文献或课题研究，在学习中研究、在研究中学习，遇到了问题深入分析研究，用已有知识学习求解问题所需要的知识，使学习和研究成为一个互动的过程。在研讨中积累知识、培养能力和锻炼思维。</span> -->
					            </div>
					            <div style="margin-top: 20px">
					                <span style="font-weight: bold;display: inline-block ;height: fit-content; margin-bottom :20px; ">教学环节
					                </span><br>
					
					                <span style="display: inline-block; text-align: left; margin-left: 60px;width: 100%;">一、创设情境，激发兴趣</span><br>
					                <span style="display: inline-block; text-align: left; margin-left: 60px;width: 100%;">二、课文品读，感受新知</span><br>
					                <span style="display: inline-block; text-align: left; margin-left: 60px;width: 100%;">三、拓展阅读，知识延伸</span><br>
					                <span style="display: inline-block; text-align: left; margin-left: 60px;width: 100%;">四、知识应用，写作训练</span><br>
					                <span style="display: inline-block; text-align: left; margin-left: 60px;width: 100%;">五、评价反馈，修正完善</span><br>
					            </div>
					        
					        </div>
                            <div v-else-if="currentTab === '9'">
					            <div>
					                <span style="font-weight: bold;display: inline-block ;height: fit-content; margin-bottom :20px; ">模式简介
					                </span>
					                <div style="text-align: left">该模式注重学生对古诗的感知和体验，通过扩展阅读和对照比较，学生能够进一步拓展对古诗的感知和体验，从而更好地欣赏和理解古诗的美。
                                    </div>
					                <!-- <span style="display:inline-block ;width:100%;text-align: left">在教学的过程中，教师把研究的项目及方向和教学课程相结合，在教师的指导下，通过阅读文献或课题研究，在学习中研究、在研究中学习，遇到了问题深入分析研究，用已有知识学习求解问题所需要的知识，使学习和研究成为一个互动的过程。在研讨中积累知识、培养能力和锻炼思维。</span> -->
					            </div>
					            <div style="margin-top: 20px">
					                <span style="font-weight: bold;display: inline-block ;height: fit-content; margin-bottom :20px; ">教学环节
					                </span><br>
					
					                <span style="display: inline-block; text-align: left; margin-left: 60px;width: 100%;">一、熟知诗人，明晓题意</span><br>
					                <span style="display: inline-block; text-align: left; margin-left: 60px;width: 100%;">二、理解诗意，体会诗情</span><br>
					                <span style="display: inline-block; text-align: left; margin-left: 60px;width: 100%;">三、扩展阅读，知识迁移</span><br>
					                <span style="display: inline-block; text-align: left; margin-left: 60px;width: 100%;">四、对照比较，知识总结</span><br>
					              
					            </div>
					        
					        </div>
					    </el-main>
					    </el-container>
					    </el-container>
					    
					</div>
					<!-- 教学模式-end -->
				</div>
                
                <div style="margin:0 auto;text-align: center;" >
                    
                        <el-button  type="primary"  @click="submitForm">
                            <i class="el-icon-circle-check"></i>	
                            智能生成教案</el-button>
                            <!-- <el-button  type="primary" v-if="!checkboxValues.includes(requiredOption)"  @click="submitForm">
                            <i class="el-icon-circle-check"></i>	
                            智能生成教案</el-button> -->
                 </div>
                </div>
                                                            
        </div>
       </el-form>
    </div>


    
    

</template>

<script >
	import imgAI from '@/assets/AI助手@2x.svg'
    import draggable from "vuedraggable";
    //import { ref } from 'vue'
    //import { VueDraggable } from 'vue-draggable-plus'
    // import Logo from '../assets/JNU_Horizontal.jpg'
    import Logo from '../assets/JNU.jpg'
    // import Logo from '@/assets/robot.png'



    export default {
        components:{
                draggable
            },
        data() {
            return {
                //实验顺序
                order:'',
				//时间
				startTime: null, // 计时开始时间
				timerId: null, // 定时器ID   
				elapsedTime: '00:00:00', // 已运行时间
				matchT:'',
				studyPath:'',
				img_AI:imgAI,
                enabled: true,
				teachMode:[
				],
            list: [
                { name: "情境创设，课程导入", id: 0 },
                { name: "分析问题，明确目标", id: 1 },
                { name: "动手实践，探究新知", id: 2 },
                { name: "课堂总结，建构概念", id: 3 },
                { name: "知识巩固，迁移应用", id: 4 }
                
            ],
            newItemTemplate: { id: null, name: '' }  ,  
            dragging: false,

                Logo : Logo,
                items: [
                    {content :'情境创设，课程导入' }, 
                    {content :'分析问题，明确目标' }, 
                    {content :'动手实践，探究新知' }, 
                    {content :'课堂总结，建构概念' }, 
                    {content :'知识巩固，迁移应用' }] ,
                //form: {
                IsVisible:true,
                currentTab:'1',//选中的教学模式序列号
                form:{},
                checkboxValues:[],
                // requiredOption:'教学过程',
                selectkey:0 ,
                textarea :'',
                select_value:'',
                select_options: [{
                value: '练习课',
                label: '练习课'
                }, {
                value: '新授课',
                label: '新授课'
                }, {
                value: '讲评课',
                label: '讲评课'
                }, {
                value: '复习课',
                label: '复习课'
                }, {
                value: '自定义课型',
                label: '自定义课型'
                }],
                num :1,
                basic_info: [],
				basic_options: [{
					value:'初中',
					label: '初中',
					children:[{
						value:'语文',
						label: '语文',
						children:[{
							value:'部编版',
							label: '部编版',
							children:[{
								value:'七年级上',
								label: '七年级上',
								children:[{
									value:'毛泽东编写的《纪念白求恩》',
									label: '纪念白求恩/毛泽东',
								},
								]
							},
							{
								value:'八年级上',
								label: '八年级上',
                                children:[{
									value:' 李白编写的《渡荆门送别》',
									label: '渡荆门送别/李白',
								},
								]
							},
                            {
								value:'八年级上',
								label: '八年级上',
                                children:[{
									value:' 《孟子三章》中的《生于忧患，死于安乐》',
									label: '生于忧患，死于安乐《孟子三章》',
								},
								]
							},
                            {
								value:'九年级上',
								label: '九年级上',
                                children:[{
									value:'余光中编写的《乡愁》',
									label: '《乡愁》/余光中',
								},
								]
							}
							],
						},
                    
                    ],
						
					},{
						value:'数学',
						label: '数学',
                        children:[{
							value:'人教版',
							label: '人教版',
							children:[{
								value:'七年级上',
								label: '七年级上',
								children:[{
									value:'正数和负数',
									label: '正数和负数',
								},
								]
							},
							{
								value:'七年级下',
								label: '七年级下',
                                children:[{
									value:' 消元——解二元一次方程组',
									label: '消元——解二元一次方程组',
								},
								]
							},
                            {
								value:'八年级上',
								label: '八年级上',
                                children:[{
									value:' 平方差公式',
									label: '平方差公式',
								},
								]
							},
                            {
								value:'九年级上',
								label: '九年级上',
                                children:[{
									value:'中心对称图形',
									label: '中心对称图形',
								},
								]
							}
							],
						},
                    
                    ],
					},{
						value:'英语',
						label: '英语',
                        children:[{
                            value:'七年级上',
								label: '七年级上',
								children:[{
									value:'Good morning！',
									label: 'Good morning！',
								},
								]

                        },{
                            value:'七年级上',
								label: '七年级上',
								children:[{
									value:'what color is it?',
									label: 'what color is it?',
								},
								]
                            
                        },{
                            value:'八年级上',
								label: '八年级上',
								children:[{
									value:'I‘m more outgoing than my sister',
									label: 'I‘m more outgoing than my sister',
								},
								]
                        },{
                            value:'八年级上',
								label: '八年级上',
								children:[{
									value:'what‘s the best movie theater?',
									label: 'what‘s the best movie theater?',
								},
								]
                        }]
					}
					]
				},],
		
				// basic-options -end
                course_info: [],
                course_options_Map: {
                  'Chinese:primary:bubianban54':[
                    {
                      value :'one_F',
                      label :'一年级上',
                      children :[
                        {
                          value :'SZ',
                          label :'识字',
                          children :[
                            {
                              value :'TDR',
                              label :'1.天地人'
                            },
                            {
                              value :'JMSHT',
                              label :'2.金木水火土'
                            }
                            ,
                            {
                              value :'KEM',
                              label :'3.口耳木'
                            }
                
                          ]
                        }
                      ]
                    }
                  ],
                  'Chinese:primary:bubianban':[
                    {
                        value :'one_S',
                        label :'一年级下',
                        children :[
                        {
                              value :'WSXL',
                              label :'1.我上学了'
                            },
                            {
                              value :'SZ',
                              label :'2.识字(一)'
                            }
                            ,
                            {
                              value :'HYPY',
                              label :'3.汉语拼音'
                            }
                        ]
                    }
                  ]
                },
                course_options:[],
                modeList:['自定义教学','探究式教学','讲授式教学','协作式教学','讲座式教学','情景式教学','研究式教学','语文阅读课教学','古诗阅读教学模式','基于问题的教学','概念获得式教学','抛锚式教学','"设问—导学"教学'],
                radio:'',
				
            
               // }
            };

        },
		mounted() {
            //this.order=this.$route.params.order;
            // let index1 = sessionStorage.getItem('index');
            // let index2 = parseInt(index1);
            // this.order=index2;
            // console.log(this.order)
			this.getStudyInfo();
		},
        methods: {
			// 开始计时
			    startTimer() {  
			      if (!this.isTimerRunning) {  
			        this.startTime = new Date();  
			        this.timerId = setInterval(() => {  
			          this.updateElapsedTime();  
			        }, 1000); // 每秒更新一次时间  
			        this.isTimerRunning = true;  
			      }  
			    },  
			    // 更新已运行时间  
			    updateElapsedTime() {  
			      const now = new Date();  
			      const diff = now - this.startTime;  
			      const hours = Math.floor(diff / (1000 * 60 * 60));  
			      const minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));  
			      const seconds = Math.floor((diff % (1000 * 60)) / 1000);  
			      this.elapsedTime = `${String(hours).padStart(2, '0')}:${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`;  
			    },
			//获取实验的教案主题以及实验路径
			getStudyInfo(){
				// this.matchT=this.$route.params.matchTheme;
				// this.studyPath=this.$route.params.path;
                // this.order=this.$route.params.order+1;
                // this.radio=this.$route.params.radio;
                let retrievedList = JSON.parse(sessionStorage.getItem('matchTheme'));
				this.matchT=retrievedList[parseInt(sessionStorage.getItem('index'))];
				this.order=parseInt(sessionStorage.getItem('index'))+1;
				this.radio=sessionStorage.getItem('radio');
                this.studyPath = sessionStorage.getItem('path');

                // this.matchT=this.$route.params.matchTheme;
				// this.studyPath=this.$route.params.path;
                // this.order=this.$route.params.order+1;
                // this.radio=this.$route.params.radio;
			},
           
            handleAdd(){
                if (this.list.length === 10) {
                        this.$message({
                        message: '已到最大数量',
                        type: 'warning'
                        });
                        return;
                        }
                const length = this.list.length + 1
                const newId = this.getNextId
                    this.list.push({name: ``,id: newId })
            },
             getNextId() {  
            // 这里只是一个简单的示例，你可能需要根据实际情况来生成 id  
                return Math.max(...this.list.map(item => item.id)) + 1;  
            } ,
            // handleAdd(index){
            //     // 确保index不超过数组长度，否则将其设置为数组长度（即插入到末尾）  
            //     if (index >= this.list.length) {  
            //         index = this.list.length;  
            //     }  
            
            //     // 获取新元素的名称和ID，基于当前数组长度+1（如果是插入到末尾）  
            //     const newLength = this.list.length + 1; // 如果插入到末尾，使用当前长度+1  
            //     const newName = `${newLength}`;  
            //     const newId = `${newLength}`;  
            
            //     // 在index的下一个位置插入新元素  
            //     this.list.splice(index + 1, 0, {  
            //         name: newName,  
            //         id: newId  
            //     }); 
            //     // const length = this.list.length + 1
            //     //     this.list.push({
            //     //         name: `Juan ${length}`,
            //     //         id: `${length}`
            //     //     })
            // },
            handleRemove(index){
                if(this.list.length === 1){
                    this.$message({
                        message: '请至少保留一个教学环节',
                        type: 'warning'
                        });
                        return;
                        }
                
                this.list.splice(index, 1);  
                
            },
            addItem() {
                this.items.push('');
            },
            removeItem(item_index) {
                if (this.items.length === 1) {
                        this.$message({
                        message: '请至少保留一个教学环节',
                        type: 'warning'
                        });
                        return;
                        }
                this.items.splice(item_index, 1);
            },
            indexToChar(item_index) {
                const chineseNumber = ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十'];
                return chineseNumber[item_index];
                // return String.fromCharCode(65 + item_index); // 将索引转换为字母，例如：0 -> A, 1 -> B, 2 -> C, ...
            },
            handleMenuSelect(index){
                this.currentTab = index;    
            },
            Vision(){
                this.IsVisible = !(this.IsVisible);
            },
            display_selected(select_value){
                // console.log('select !!');
                // console.log(select_value);
            },
            handleChange(value) {
                // console.log(value);
            },
			// 请选择基本信息
            display_basic(basic_info){
                // console.log('this is basic_info 3');
                // console.log(basic_info);
                // console.log('now it is course_options_Map 4');
                // console.log(this.course_options_Map);
            },
            display_course(course_info) {
                // console.log('this is course_info 1' );
                // console.log(course_info);
                // console.log('this is basic_options 2');
                // console.log(this.basic_options)
            },
            display_input(textarea){
                //console.log(textarea)
            },
           showSelect(checkboxValues){
                //console.log(checkboxValues)
           },
           ClearSelection(){
                this.checkboxValues=[];
           },
		   // 点击 - 智能生成教案 - 跳转页面 - lessonGen.vue
           submitForm(){
            //自定义
            let freeMode=[];
            let tab=this.currentTab;
            if(this.currentTab=='1'){
                //console.log('list:'+this.list[this.list.length-1].name);
                for(var i=0;i<this.list.length;i++){
                    freeMode.push(this.list[i].name);
                }
            }else{
                //tab=this.currentTab;
            }
			   const t=this.basic_info;
			   const cv=this.checkboxValues;

               
               
               console.log(cv);
			   // this.$router.push({name:'lessonGen',
			   // 				    params:{
			   // 					teachInfo:t,
						// 		teachStru:cv
			   // 					}
			   // });
			   //LessonEditByAI
			   //实验路径
			   const p=this.studyPath;
			   const st=this.startTime;
               const o=this.order;
               const r=this.radio;
               const th=this.matchT;
               console.log('click:'+freeMode);
               //teachInfo teachStru startTime tab freemode
               sessionStorage.setItem('teachInfo', JSON.stringify(t));
               sessionStorage.setItem('teachStru', JSON.stringify(cv));
			   //sessionStorage.setItem('startTime',st);
			   sessionStorage.setItem('tab',tab);
               sessionStorage.setItem('freemode', JSON.stringify(freeMode));
			   //实验study路径
			   this.$router.push({name:p,
			   				    params:{
                                matchTheme:th,
			   					teachInfo:t,
			   					teachStru:cv,
								startTime:st,
                                order:o,
                                radio:r,
                                tab:tab,
                                freemode:freeMode,
			   					}
			   });
			   //实验study路径-多人协同
			   // this.$router.push({name:'lessonGen',
			   // 				    params:{
			   //                  matchTheme:th,
			   // 					teachInfo:t,
			   // 					teachStru:cv,
			   //                  tab:tab,
			   //                  freemode:freeMode,
			   // 					}
			   // });

           },


           checkMove: function(e) {
                // window.console.log("Future index: " + e.draggedContext.futureIndex);
                
            }
        },

        watch: {
            
            basic_info(newVal){
                this.course_options =[];
                //将this.course_options初始化
                // console.log('this is last course_info');
                // console.log(this.course_info);
                // this.course_info=[];
                // console.log('this is after course_info');
                // console.log(this.course_info);
                //将this.course_info初始化，如果没有初始化，会保留上一次选择的结果
                
                // console.log('this is newVal 5');
                // console.log(newVal);
                // console.log('this is basic_info 6');
                // console.log(this.basic_info);
                let keyToMatch = newVal.join(':');
                console.log(keyToMatch);
                if(keyToMatch in this.course_options_Map){
                    console.log('this it is 7');
                    console.log(this.course_options_Map);
                    const tempOptions = this.course_options_Map[keyToMatch];
                    this.course_options = tempOptions.map(option =>({
                        value :option.value,
                        label :option.label,
                        children :option.children
                    }));
                    // this.course_options = this.course_options_Map[newVal];
                    //console.log('Options Changed')
                }
                else {
                    //console.log('not in 8');
                    this.course_options =[];
                }
            },
            // select_value(newVal){
            //     console.log(this)
            // }
        }

    };


</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
	.el-avatar{
		/* border: 10px solid #409EFF; */
		box-shadow: rgba(64, 158, 255, 0.4) 0px 2px 8px 0px;
		
	}
	.hayabox{
		margin-left: 8%;
		margin-top: 1.9375rem;
		margin-bottom: 0.9375rem;
	}
	.animate__animated.animate__pulse {
	  /* --animate-duration: 100s; */
	  --animate-duration: 2s;
	}
	.haya{
		font-family: 'Avenir', Helvetica, Arial, sans-serif;
		font-size: 18px;
		padding-top: 0.9375rem;
		

		margin-bottom: 0.9375rem;
		color:darkslategrey;
		padding-left: 10px;
	}
	.el-select{
		margin-right: 1.25rem;
	}
	.el-cascader{
		width: 35%;
	}

    .el-checkbox {
		margin-bottom: 0.725rem;
		margin-right:5px;
	}
    .user-defined{
        display: flex;  
        align-items: center; /* 垂直居中 */  
        justify-content: space-between; /* 水平两端对齐，适用于按钮在输入框之后的情况 */  
        margin-bottom: 10px; /* 添加间距以便每个输入行之间有所区分 */  
    }

    .draggable-container{
        display:flex;
        /* margin-left:200px; */
        justify-content: center; 
        /* 水平居中 */  
    }

    .ghost {
    opacity: 0.5;
    background: #c8ebfb;
    }
 
  
    .list-group {  
        display: flex;  
        
        flex-direction: column;  
        padding-left: 0;  
        margin-bottom: 0;  
        width: 600px;  
    }  
    
    .list-group .list-group-item { /* 注意这里添加了空格来确保选择器的正确应用 */  
        cursor: move;  
        position: relative;  
        display: block;  
        padding: 0.75rem 1.25rem;  
        margin-bottom: -1px;  
        background-color: #fff;  
        border: 1px solid rgba(0,0,0,.125);  
    }  
    Image{
        /* object-fit: cover; */
        mix-blend-mode: darken;
    }
    .backgroundPlate{
        background-color: white;
        width: 1300px;
        margin: 0 auto;
        border-radius: 8px;
        padding-top: 30px;
		animation: fadeIn; /* referring directly to the animation's @keyframe declaration */
		animation-duration: 1s; /* don't forget to set a duration! */
    }

    .title{
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .content-container{
        flex: 1;
        padding :10px
    }
    .SetBackground{
		margin-top: 0px;
        background: linear-gradient(to top,  #fff,rgb(190, 227, 255));
		margin-bottom: 15px;
    }

    .container-with-shadow {
    /* box-shadow: 0 2px 4px rgba(0, 0, 0, 0.5);  */
    /* 阴影效果 */
   
    }

    .el-header {
        background-color: #B3C0D1;
        color: #333;
        text-align: center;
        line-height: 60px;
    }
    
    .el-aside {
        background-color: #D3DCE6;
        color: #333;
        text-align: center;
        line-height: 400px;
    }
  

    .el-menu-item{
        background-color:white;
        border: 1px solid #ccc;
    }
    .el-main {
        /* background-color: #E9EEF3; */
        color: #333;
        text-align: center;
        /* line-height: 200px; */
    }
    .box-card {
        width: 1000px;
    }
    .cblock span,.cblock el-input{
        
        display: inline-block;
        vertical-align: middle;
        
    }
    .container{
        display: flex;
       
    }
    .block{
        vertical-align: middle;
        text-align: left;   
		margin-left: 5%;
		margin-bottom: 0.925rem;
		
    }
    .demonstration{
        font-weight: bold;
        margin-left: 50px;
        margin-right: 40px;
        width: 112px;      
        display:inline-block;
    }


   ::v-deep .el-checkbox__input.is-disabled+span.el-checkbox__label{
        color:#409EFF;
    }

    ::v-deep .el-checkbox__input.is-disabled.is-checked .el-checkbox__inner {
        background-color:#409EFF;
    }
 

    ::v-deep .el-form-item {
        text-align:  center;
    }

    .inputtext {
        display: flex;
        align-items: center;
        justify-content: center;
    }
    

    
    .container {
		
		border:1px solid #ccc;
        display: flex;
		width: 80%;
		
    }
    .box {
        width: 100px;
        display: flex;
        align-items: center;
    }

    .box>*{
        margin-right: 10px;
    }
    a {
        color: #42b983;
    }
    
   
    
</style>