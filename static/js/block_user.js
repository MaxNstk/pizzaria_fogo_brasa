async function blockUser(userId, is_active){
    const response =  await axios({
        headers: {"X-CSRFToken": CONTEXT.CSRF_TOKEN,},
        url : `api/v1/user/${userId}/`,
        method : 'patch',    
        datatype: 'json',
        data: {'is_active': !is_active},
        })
    if (response.status == 200){
        window.location.reload()
        return
    }
}

