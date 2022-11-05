async function handleObjectActivation(objectId, IsActive, path){
    const response =  await axios({
        headers: {"X-CSRFToken": CONTEXT.CSRF_TOKEN,},
        url : `${path}${objectId}/`,
        method : 'patch',    
        datatype: 'json',
        data: {'is_active': !IsActive},
        })
    if (response.status == 200){
        window.location.reload()
        return
    }
}

