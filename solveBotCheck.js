async function main(){
    if(!document.querySelector('#py-sender')){
        const pythonSender = document.createElement('p')
        pythonSender.textContent = '{}'
        document.body.appendChild(pythonSender)
        pythonSender.style.bottom = '170px'
        pythonSender.style.left = `20px`
        pythonSender.style.position = 'absolute'
        document.querySelector('.fade.modal-modern.modal-modern-challenge-captcha.in.modal').style.background = 'none'
    }
}

main()