const gridTraveller=(n,m,memo={})=>{
    const key=m+','+'n';
    if(key in memo) return memo[key]
    if(n==0 || m==0){
        return 0
    }
    if(n===1 && m===1){
        return 1
    }

    memo[key]= gridTraveller(m-1,n,memo)+gridTraveller(m,n-1,memo)
    return memo[key]

}

console.log(gridTraveller(19,18))