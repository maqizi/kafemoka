import axiosInstance from './index'

const axios = axiosInstance

export const getLessondatas = () => {
	return axios.get(`http://localhost:8000/api/getLessondatas/`)
}

export const getuserLessondata = (username) => {
	return axios.post(`http://localhost:8000/api/getLessondatas/`, {
		'username': username
	})
}

export const getLessondata = (id) => {
	return axios.post(`http://localhost:8000/api/getLessondata/`, {
		'id': id
	})
}

export const delLessondata = (id) => {
	return axios.post(`http://localhost:8000/api/delectlessondata/`, {
		'id': id
	})
}

export const registerUser = (username, password) => {
	return axios.post(`http://localhost:8000/api/register/`, {
		'username': username,
		'password': password
	})
}

export const loginUser = (username, password) => {
	return axios.post(`http://localhost:8000/api/login/`, {
		'username': username,
		'password': password
	})
}

export const Insertlesson = (UserName, LessonName, Navigation, Lessoncontent) => {
	return axios.post(`http://localhost:8000/api/insertlesson/`, {
		'UserName': UserName,
		'LessonName': LessonName,
		'Navigation': Navigation,
		'Lessoncontent': Lessoncontent,
	})
}

export const resetlesson = (id, LessonName, Navigation, Lessoncontent) => {
	return axios.post(`http://localhost:8000/api/resetLessondata/`, {
		'id': id,
		'LessonName': LessonName,
		'Navigation': Navigation,
		'Lessoncontent': Lessoncontent,
	})
}

export const insertshare = (Author, Sharer, Privilege, Lessonid) => {
	return axios.post(`http://localhost:8000/api/insertshare/`, {
		'Author': Author,
		'Sharer': Sharer,
		'Privilege': Privilege,
		'Lessonid': Lessonid,
	})
}

export const getshare = (username) => {
	return axios.post(`http://localhost:8000/api/getshare/`, {
		'username': username
	})
}

export const getetherpad = (apikey, padID) => {
	return axios.get(`/api/getText`, {
		params: {
			apikey: apikey,
			padID: padID,
		}
	})
}

export const setetherpad = (apikey, padID, text) => {
	return axios.get(`/api/setText`, {
		params: {
			apikey: apikey,
			padID: padID,
			text: text,
		}
	})
}

export const createtherpad = (apikey, padID) => {
	return axios.get(`/api/createPad`, {
		params: {
			apikey: apikey,
			padID: padID,
			text:'',
		}
	})
}

export const setetherpadHtml = (apikey, padID, html) => {
	//如果修改为post，显示错误 ：401 http://localhost:8080/api/setHTML 401 (Unauthorized)
	return axios.get(`/api/setHTML`, {
		params: {
			apikey: apikey,
			padID: padID,
			html: html,
		},
		
	})
}