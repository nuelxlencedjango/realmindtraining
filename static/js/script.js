
var menuInfo = false;
var main_menu = document.getElementById("navbar-nav");
var mainContent  = document.getElementById("content");

var mainFirst = document.getElementById("header-top");


function checkToggle(){
if(menuInfo===false){
	mainFirst.style.display ="none";
    main_menu.style.display = "block";
    mainContent.style.marginTop ="330px";
	
   
    menuInfo =true;


	
}
else{
    main_menu.style.display = "none";
	mainFirst.style.display ="block";
    mainContent.style.marginTop ="30px";
    menuInfo =false;
	//console.log(main_menu);

}


}





window.onscroll = function() {myFunction()};
	
var navbar = document.getElementById("navbar");
var sticky = navbar.offsetTop;
	
function myFunction() {
	if (window.pageYOffset >= sticky) {
	    navbar.classList.add("sticky")
	  } 
	else{
		navbar.classList.remove("sticky");
	  }
	}


	
var myCarousel = document.querySelector('#myCarousel')
var carousel = new bootstrap.Carousel(myCarousel, {
  interval: 2000,
  wrap: false
})


