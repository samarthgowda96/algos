const palindrome=(string)=>{
    var str=string.split('')
    var rev=[]
    for(var i = str.length-1 ; i>=0;i--){
        rev.push(str[i])
    }
    if (rev.join()===str.join()){
        return true
    } else {
        return false

    }
}

string="RaceCar"

console.log(palindrome(string))