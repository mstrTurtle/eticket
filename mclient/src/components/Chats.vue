<template>
    <div class="phoneswrapper">
  
  <div class="phone">
    <div class="phone_head">
      <div class="title"> My Chats </div>
      <div class="icon_bubble msg"> </div>
    </div>
    <div class="divider"> </div>
    <div class="phone_body">
       <div class="chat">
         <img class="chat_avatar" src="https://randomuser.me/api/portraits/men/32.jpg">
         <div class="chat_info">
           <div class="contact_name">Patric Venturini </div>
           <div class="contact_msg">Are you planning to play anything tonight?  </div>
         </div>
         <div class="chat_status">
           <div class="chat_date">9:20 PM</div>
           <div class="chat_new grad_pb"> New </div>
         </div>
      </div>
      
      <div class="chat">
         <img class="chat_avatar" src="https://randomuser.me/api/portraits/men/11.jpg">
         <div class="chat_info">
           <div class="contact_name">Adriano Canofre </div>
           <div class="contact_msg">Dude can you help me with my motorcycle?</div>
         </div>
         <div class="chat_status">
           <div class="chat_date">8:12 PM</div>
           <div class="chat_new grad_pb"> New </div>
         </div>
      </div>
      
      <div class="chat">
         <img class="chat_avatar" src="https://randomuser.me/api/portraits/men/32.jpg">
         <div class="chat_info">
           <div class="contact_name">Patric Venturini </div>
           <div class="contact_msg">Are you planning to play anything tonight?  </div>
         </div>
         <div class="chat_status">
           <div class="chat_date">Yesterday</div>
           <div class="chat_new grad_pb"> New </div>
         </div>
      </div> 
      <div class="chat">
         <img class="chat_avatar" src="https://randomuser.me/api/portraits/men/11.jpg">
         <div class="chat_info">
           <div class="contact_name">Adriano Canofre </div>
           <div class="contact_msg">Dude can you help me with my motorcycle?</div>
         </div>
         <div class="chat_status">
           <div class="chat_date">Yesterday</div>
            
         </div>
      </div>
      
      <div class="chat">
         <img class="chat_avatar" src="https://randomuser.me/api/portraits/men/32.jpg">
         <div class="chat_info">
           <div class="contact_name">Patric Venturini </div>
           <div class="contact_msg">Are you planning to play anything tonight?  </div>
         </div>
         <div class="chat_status">
           <div class="chat_date">Yesterday</div>
            
         </div>
      </div>
      <div class="chat">
         <img class="chat_avatar" src="https://randomuser.me/api/portraits/men/11.jpg">
         <div class="chat_info">
           <div class="contact_name">Patric Venturini </div>
           <div class="contact_msg">Are you planning to play anything tonight?  </div>
         </div>
         <div class="chat_status">
           <div class="chat_date">Yesterday</div>
            
         </div>
      </div>
      
      <div class="chat">
         <img class="chat_avatar" src="https://randomuser.me/api/portraits/men/32.jpg">
         <div class="chat_info">
           <div class="contact_name">Patric Venturini </div>
           <div class="contact_msg">Are you planning to play anything tonight?  </div>
         </div>
         <div class="chat_status">
           <div class="chat_date">Yesterday</div>
            
         </div>
      </div>
    </div> <!-- phonebody -->
    
  </div>
  

</div>
</template>

<style scoped>
* { box-sizing: border-box}
body{
  font-family: 'Asap', sans-serif;
}
.phoneswrapper{
  /* display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  padding: 20px; */
}

.phone{
  /* height:  600px; */
  /* width: 300px;  */
  padding: 10px 20px;
  /* border-radius: 32px;
  border: 8px solid #3e3e3e; */
  /* overflow: hidden;
  position: relative; */
  /* box-shadow: 0px 17px 20px rgba(0, 0, 0, 0.15); */
  
  width:100vw;
  height:100vw;

}
.phone_head {
    display: flex;
    flex-direction: row;
    justify-content: space-between; 
     align-items: center;
    height: 45px;
}
.phone_head .title{
  font-size: 24px;
  font-weight: 500;
  color: #34394F;
}
.icon_bubble.msg {
    width: 30px;
    height: 30px;
    background: linear-gradient( 90deg, #d13eea, #53d9ea);
    border-radius: 50%;
}

.divider {
    height: 1px;
    width: 111%;
    background: linear-gradient( 90deg, #d13eea, #53d9ea);
    margin-bottom: 12px;
}
.grad_pb{ background: linear-gradient( 90deg, #d13eea, #53d9ea);
  color: white; 
  }
img.chat_avatar {
    width: 45px;
  height: 45px;
    border-radius: 7px;
  margin-right: 8px;
}
img.chat_avatar {
    width: 45px;
   box-shadow: 1px 6px 18px rgba(31, 37, 72, 0.45);
    border-radius: 7px;
}

.chat {
    display: flex;
    justify-content: space-between;
    padding: 15px 0px;
    border-bottom: 1px solid #d3d3d35e;
}

.contact_name {font-weight: 500;

  color: #34394F;
     font-size: 15px;
    margin-bottom: 2px;}

.contact_msg {
   
     font-size: 11px;
    color: #a5a5a5;
    font-weight: lighter;
}
.chat_info {width: 50%;}

.chat_date {
    font-size: 12px;
    color: #5a5a5a;
  margin-bottom: 2px;
}

.chat_new{
  padding: 2px 5px;
  font-size: 11px;
  border-radius: 2px;
}
.chat_status {
    width: 25%;
    display: flex;
    flex-direction: column;
    align-items: center; 
}

</style>