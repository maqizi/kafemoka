import axiosInstance from './index'

const axios = axiosInstance

export const getLessondatas = () => {
    return axios.get(`http://127.0.0.1:8000/api/getLessondatas/`)}

export const getuserLessondata = (username) => {
    return axios.post(`http://127.0.0.1:8000/api/getLessondatas/`, {'username': username})}

export const getLessondata = (id) => {
    return axios.post(`http://127.0.0.1:8000/api/getLessondata/`, {'id': id})}

export const delLessondata = (id) => {
    return axios.post(`http://127.0.0.1:8000/api/delectlessondata/`, {'id': id})}

export const registerUser = (username, password) => {
    return axios.post(`http://127.0.0.1:8000/api/register/`, {'username': username, 'password': password})}

export const loginUser = (username, password) => {
    return axios.post(`http://127.0.0.1:8000/api/login/`, {'username': username, 'password': password})}

export const Insertlesson = (UserName, LessonName, Navigation, Lessoncontent) => {
        return axios.post(`http://127.0.0.1:8000/api/insertlesson/`, 
        {'UserName': UserName, 
         'LessonName': LessonName,
         'Navigation': Navigation, 
         'Lessoncontent': Lessoncontent, 
        })}

export const resetlesson = (id, LessonName, Navigation, Lessoncontent) => {
        return axios.post(`http://127.0.0.1:8000/api/resetLessondata/`, 
        {'id': id,  
        'LessonName': LessonName,
        'Navigation': Navigation, 
        'Lessoncontent': Lessoncontent, 
        })}    

export const insertshare = (Author, Sharer, Privilege, Lessonid) => {
        return axios.post(`http://127.0.0.1:8000/api/insertshare/`, 
        {'Author': Author, 
        'Sharer': Sharer, 
        'Privilege': Privilege,
        'Lessonid': Lessonid,
        })}  

export const getshare = (username) => {
    return axios.post(`http://127.0.0.1:8000/api/getshare/`, {'username': username})}

export const getetherpad = (apikey,padID) => {
    return axios.get(`/api/getText`, {
        params: {
            apikey: apikey,
            padID: padID,
          }})}

export const setetherpad = (apikey,padID,text) => {
    return axios.get(`/api/setText`, {
        params: {
            apikey: apikey,
            padID: padID,
            text: text,
            }})}
			
export const setetherpadHtml = (apikey,padID,text) => {
    return axios.get(`/api/setHTML`, {
        params: {
            apikey: apikey,
            padID: padID,
            html: text,
            }})}
    
export const createtherpad = (apikey,padID) => {
    return axios.get(`/api/createPad`, {
        params: {
            apikey: apikey,
            padID: padID,
            }})}

export const insertstudyorder = (UserName, Subject,Order1, Order2, Order3, Order4) => {
    return axios.post(`http://127.0.0.1:8000/api/setorder/`, 
    {'UserName': UserName, 
    'Subject': Subject, 
    'Order1': Order1, 
    'Order2': Order2,
    'Order3': Order3,
    'Order4': Order4,
    })}  

export const getstudyorder = (UserName) => {
    return axios.get(`http://127.0.0.1:8000/api/setorder/`, 
    {
        params:{'UserName': UserName,}
    })}   

export const insertstudyorderc = (UserName,OrderName) => {
    return axios.post(`http://127.0.0.1:8000/api/setorderc/`, 
    {'UserName': UserName, 
    'OrderName': OrderName, 
    })}  

export const getstudyorderc = (UserName) => {
    return axios.get(`http://127.0.0.1:8000/api/setorderc/`, 
    {
        params:{'UserName': UserName,}
    })}   

export const insertstudtime = (Study, UserName, Subject, TotalTime , TextSum , LessonContent) => {
    return axios.post(`http://127.0.0.1:8000/api/setstudy/`, 
    {'Study': Study,
    'UserName': UserName, 
    'Subject': Subject, 
    'TotalTime': TotalTime, 
    'TextSum': TextSum,
    'LessonContent': LessonContent,
    })} 

export const inserthistoryc = (Send_username , Receive_username , Content  , Sendtime  ,StartTime,EndTime, Rate, AcceptOrRejectTime ) => {
    return axios.post(`http://127.0.0.1:8000/api/sethistoryc/`, 
    {'Send_username': Send_username,
    'Receive_username': Receive_username, 
    'Content': Content, 
    'Sendtime': Sendtime,
    'StartTime':StartTime,
    'EndTime':EndTime,
    'Rate': Rate,
    'AcceptOrRejectTime': AcceptOrRejectTime,
    })} 

export const inserthistoryaia = (Send_username , Receive_username , SelectText, Content  , Sendtime  ,StartTime,EndTime, Rate, AcceptOrRejectTime ) => {
    return axios.post(`http://127.0.0.1:8000/api/sethistoryaia/`, 
    {'Send_username': Send_username,
    'Receive_username': Receive_username, 
    'SelectText': SelectText,
    'Content': Content, 
    'Sendtime': Sendtime,
    'StartTime':StartTime,
    'EndTime':EndTime,
    'Rate': Rate,
    'AcceptOrRejectTime': AcceptOrRejectTime,
    })} 

export const getuserid = (username) => {
    return axios.get(`http://127.0.0.1:8000/api/getuserid/`, 
    {
        params:{'username': username,}
    })}   

export const getsubjectnum = (Subject) => {
    return axios.get(`http://127.0.0.1:8000/api/getsubjectnumber/`, 
    {
        params:{'Subject': Subject,}
    })} 
	
export const retrieveInfo = (db_name,query) => {
    return axios.post(`http://127.0.0.1:8000/api/retrieve/`, 
    {'db_name': db_name,
    'query': query,
    })} 