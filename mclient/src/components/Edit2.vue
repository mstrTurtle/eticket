<template>
  <div class="container">
    <div class="iphone">
      <div class="header">
        <div class="order-summary">
          <div class="order-status">Arriving date</div>
          <div class="order-date">
            19 April, 2023
          </div>
          <div class="order-day">
            Friday
          </div>
        </div>
        <div class="action-btn">
          <!-- <div class="back-btn" @keyup="onHide"><i class="far fa-long-arrow-left"></i></div> -->
        </div>
      </div>
      <!-- <div class="hero-img-container">
        <div class="triangle1"></div>
        <div class="arc"></div>
        <div class="pattern"></div>
        <img src="https://drive.google.com/uc?id=15iXUI6DkRr5Zcp0yH5uF2U47ycr-WzUY" class="hero-img">
      </div> -->
      <div class="order-status-container">
        <div class="status-item first">
          <div class="status-circle"></div>
          <div class="status-text">
            today
          </div>
        </div>
        <div class="status-item second">
          <div class="status-circle"></div>
          <div class="status-text">
            Shipped
          </div>
        </div>
        <div class="status-item">
          <div class="status-circle"></div>
          <div class="status-text green">
            <span>Out</span><span>for delivery</span>
          </div>
        </div>
        <div class="status-item">
          <div class="status-circle"></div>
          <div class="status-text green">
            <span>Ariving</span>
            <span>03&nbsp;-&nbsp;21</span>
          </div>
        </div>
      </div>
      <div class="order-details-container">
        <!-- <div class="odc-header">
          <div class="cta-text">See your product details</div>
          <div class="cta-button-container">
            <button class="cta-button" @keyup="onShow">View</button>
          </div>
        </div> -->
        <div class="odc-wrapper">
          <div class="odc-header-line">
            工单详情
          </div>
          <div class="odc-header-details">
            你的工单详情 (单号 040-904-790)
          </div>
          <div class="product-container">
            <div class="product">
              <div class="product-photo">
                <!-- <img src="https://s3.eu-central-1.amazonaws.com/sneakerjagers.com/products/396x396/92074.jpg"
                  class="img-photo"> -->
              </div>
              <div class="product-desc">
                <span>Nike Air Jordan 1</span>
                <span>9740 INR</span>
              </div>
            </div>
            <div class="product">
              <div class="product-photo">
                <!-- <img src="https://s3.eu-central-1.amazonaws.com/sneakerjagers.com/products/396x396/77674.jpg"
                  class="img-photo"> -->
              </div>
              <div class="product-desc">
                <span>Alex rider: Never say die Novel 12</span>
                <span>655 INR</span>
              </div>
            </div>
          </div>
          <a href="/">
            <div class="cancellation">
              提交表单
            </div>
          </a>



          <div class="shipping-desc">你的流转选项</div>

          <div class="shipping-address">
            前进<br>
            后退<br>
          </div>
          <a href="/">
            <div class="cancellation">
              提交表单
            </div>
          </a>
        </div>
      </div>
    </div>


</div></template>

<script >

import { ref, onUpdated, onBeforeUpdate } from 'vue'

import anime from "animejs";

function onShow(){
  cta_button_hide.play();
}

function onHide(){
  if(drawer_open) {
  slidedown.play();
  cta_button_show.play();
  }
}

function show_hideCTA(param){
    document.querySelector(".cta-button").style.display=param;
     document.querySelector(".cta-text").style.display=param;
     console.log('shCTA')
}

const onU = ()=>{

  //anime.js library
let drawer_open = false;

// document.querySelector(".cta-button").addEventListener("mouseup",function(){
//   cta_button_hide.play();
// })

// document.querySelector(".back-btn").addEventListener("mouseup",function(){
//   if(drawer_open) {
//   slidedown.play();
//   cta_button_show.play();
//   }
// })

let cta_button_show = anime({
    targets: ['.cta-button','.cta-text'],
    translateY: ['-15','0'],
    opacity: ['0','1'],
    easing: 'easeInOutSine',
    delay: anime.stagger(200),
    autoplay: false,
    // loop: false
  duration: 500,
  complete: function(){
    }
  });

let cta_button_hide = anime({
    targets: ['.cta-button','.cta-text'],
    translateY: ['0','-15'],
    opacity: ['1','0'],
    easing: 'easeInOutSine',
    delay: anime.stagger(200),
    autoplay: false,
    // loop: false
  duration: 500,
  complete: function(){
      slideup.play();
    drawer_open = true;
    }
  });


let slidedown = anime({
    targets: '.order-details-container',
    translateY: ['-560','-40px'],
   duartion: 1000,
    autoplay: false,
    begin: function(){
      show_hideCTA("block");
      drawer_open = false;
    }
})

let slideup = anime({
    targets: '.order-details-container',
    translateY: ['-40px','-560px'],
    autoplay: false,
    begin: function(){
     show_hideCTA("none");
    }
})
}

export default {
  props: {
    transition: {
      type: String,
      default: "fade",
    },
  },
  setup(props) {
    onUpdated(onU)
  }
}


</script>

<style scoped>
@import url('https://fonts.googleapis.com/css?family=Roboto:400,500,700');

* {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

body {
  font-family: 'Roboto', sans-serif;
  font-weight: 400;
  background-color: #CFDBEA;
}

a {
  text-decoration: none;
  color: white;
}

.container {
  display: flex;
  justify-content: center;
  align-content: flex-start;
  position:relative;
  /* height: 100vh; */
  width: 100vw;
}

.iphone {
  padding-top: 20px;
  background-color: #F4F4FB;
  /* height: 812px; */
  width: 375px;
  box-shadow: 0 1px 5px -1px rgba(0, 0, 0, 0.3), inset 0 0 0 1px rgba(0, 0, 0, 0.15);
  /* overflow: hidden; */
  position: relative;
  z-index: 2;
  /* transform:scale(0.8); */
  /* transform-origin: top center; */
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 12%;
}

.order-summary {
  margin-left: 1.5rem;
  padding: 1rem;
  display: flex;
  flex-direction: column; 
}

.order-summary > div {
  margin: 6px;
}

.order-status {
  color: #338A9A;
  font-size: 0.9rem;
  font-weight: 700;
  letter-spacing: 0.5px;
}

.order-date {
  font-size: 1.5rem;
  font-weight: 700;
}

.order-day {
  color: #338A9A;
  font-size: 0.9rem;
  font-weight: 300;
  letter-spacing: 0.5px;
}


.order-status-container {
  z-index: 3;
  display:flex;
  width: 100%;
  height: 25.5%;
  justify-content: space-evenly;
  align-items: center;
  background-color: white;
  border-top-right-radius: 20px;
  border-top-left-radius: 20px;
  position: relative;
   box-shadow: 0 14px 28px rgba(0,0,0,0.02), 0 10px 10px rgba(0,0,0,0.2);
}

.order-status-container::before {
  content:'';
  position:absolute;
  width: 70px;
  height: 3px;
  background-color: #EAEBFF;
  opacity: 0.8;
  border-radius: 2px;
  top:20px;
}

.status-item {
  display:flex;
  flex-direction:column;
  justify-content: flex-start;
  align-items: center;
  height: 150px;
  padding-top: 20px;
}

.status-item > div {
   margin: 10px;
}

.status-circle {
  height: 20px;
  width: 20px;
  background-color: #665CF5;
  border-radius: 50%;
  border: 5px solid white;
  box-shadow: 0 10px 20px rgba(0,0,0,0.19), 0 6px 6px rgba(0,0,0,0.23);
  z-index: 5;
  transition: all 0.2s;
  cursor: pointer;
}

.status-circle:hover {
  transform: scale(1.2);
  box-shadow: 0 14px 28px rgba(0,0,0,0.25), 0 10px 10px rgba(0,0,0,0.22);
}

.status-text {
  font-size: 0.8rem;
  font-weight: 500;
}

.status-text span {
  display: block;
  text-align: center;
  padding: 2px;
}

.green {
  color: #338A9A;
}

.first::before {
  content:'';
  height: 4px;
  width: 70px;
  background-color: #5858EF;
  position:absolute;
  z-index:4;
  top: 83px;
  left: 60px;
}

.second::before {
  content:'';
  height: 4px;
  width: 210px;
  background-color: #5858EF;
  position:absolute;
  z-index:4;
  top: 83px;
  left: 100px;
  opacity:0.2;
}

.order-details-container {
  position: relative;
  z-index: 6;
  /* height: 900px; */
  background-color: #767EEF;
  border-top-right-radius: 20px;
  border-top-left-radius: 20px;
  padding-top: 20px;
  transform:translateY(-50px);
  box-shadow: 0 10px 20px rgba(0,0,0,0.19), 0 6px 6px rgba(0,0,0,0.23);  
  cursor: default;
}

.odc-header {
  display: flex;
  justify-content: center;
  align-items: flex-start;
}

.cta-text {
  margin-top: 40px;
  margin-right: 25px;
  color: white;
  font-size: 0.9rem;
  text-shadow: 1px 1px 2px rgba(255,255,255,0.18);
}

.cta-button {
  margin-top:20px;
  padding: 20px 40px;
  background-color: #4E4DED;
  border: 0;
  border-radius: 10px;
  color: white;
  font-size: 1rem;
  font-weight: 500;
  box-shadow: 0 10px 20px rgba(0,0,0,0.10), 0 6px 6px rgba(0,0,0,0.05);
  animation: shadow-pulse 1s infinite;
  cursor:pointer;
}

@keyframes shadow-pulse
{
     0% {
          box-shadow: 0 0 0 0px rgba(255, 255, 255, 0.2);
     }
     100% {
          box-shadow: 0 0 0 35px rgba(255, 255, 255, 0);
     }
}

.cta-button:focus {
  outline:none;
}

.order-details-container::before {
  content:'';
  position:absolute;
  width: 70px;
  height: 3px;
  background-color: #EAEBFF;
  opacity: 0.8;
  border-radius: 2px;
  top:20px;
  left: 150px;
}

.odc-wrapper {
  margin:30px;
}

.odc-header-line {
  margin-top:30px;
  color: white;
  font-size: 1.5rem;
  font-weight: 500;
  margin-bottom: 40px
}

.odc-header-details {
  color:white;
  font-weight: bold;
  margin-bottom: 20px;
}

.product-container {
  background-color: #828AF1;
  border-radius: 20px;
  padding: 10px;
}

.product {
  display: flex;
  justify-content: flex-start;
  align-items: center;
}

.product span {
  display: block;
  color: white;
  margin-left: 25px;
  margin-bottom: 8px;
  flex-grow: 1;
}

.product span:first-child {
  font-weight: 300;
  font-size: 0.8rem;
}

.product span:last-child {
  font-weight: 500;
  font-size: 1.3rem;
}

.img-photo {
  width: 90px;
  transform: rotate(-35deg)
}

.cancellation {
  margin-top: 20px;
  background-color: #828AF1;
  border-radius: 20px;
  padding: 30px 20px;
    color:white;
  font-weight: bold;
  margin-bottom: 20px;
  text-align: center;
}

.shipping-desc {
  color:white;
  font-weight: bold;
  margin-bottom: 20px;
}

.shipping-address {
   margin-top: 20px;
  background-color: #828AF1;
  border-radius: 20px;
  padding: 20px 20px;
    color:white;
  font-weight: bold;
  margin-bottom: 20px;
 
}

.footer {
 position: absolute;
 bottom: 15px;
 right: 15px;
 font-size: 0.9rem;
}

.footer small {
    font-size: 0.7rem;
}

.footer a {
    color: #3273dc;
    cursor: pointer;
    text-decoration: none;
    border-bottom: 2px solid rgba(50,115,220,.1);
    padding-bottom: 2px;
}

.footer a:hover {
    color: #1e57b4;
    border-bottom-color: #1e57b4;
}
</style>