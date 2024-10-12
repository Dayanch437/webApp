const heartButtons = document.querySelectorAll ('.heart-btn');

heartButtons.forEach(button => {
    button.addEventListener('click',function() {
        if (this.classList.contains('active')){
            this.classList.remove('active');
        }else{
            this.classList.add('active');
            showFloatingNumber(this.querySelector('.floating-number'));
        }
    });
});
function showFloatingNumber(showFloatingNumber){
    showFloatingNumber.classList.add('active');
    setTimeout(()=> {
        showFloatingNumber.classList.remove('active');
    } , 500);
}
function toggleMenu() {
    const burger =document.querySelector('.burger-menu');
    const navMenu = document.getElementById('nav-menu');
    const body = document.body;
    body.classList.toggle('active')
    burger.classList.toggle('active');
    navMenu.classList.toggle('active');
}

