async function blockUser(userId){
    debugger
    const {data} =  await axios.get(`api/v1/user/${userId}/`,{
        method: 'get',
        }) 

    const response =  await axios({
        headers: {"X-CSRFToken": CONTEXT.CSRF_TOKEN,},
        url : `api/v1/user/${userId}/`,
        method : 'patch',    
        datatype: 'json',
        data: {'is_active': !data.is_active}
        })
    console.log(response);
}

