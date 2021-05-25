export const isAuthenticated = _ => {
    return true;
}

export const storeToken = (token)=>{
    
    localStorage.setItem("token", JSON.stringify(token));
}

export const removeToken = ()=>{
    localStorage.removeItem("token");
}