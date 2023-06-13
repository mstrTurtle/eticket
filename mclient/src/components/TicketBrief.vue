<template>
    <div class="card">
        <div class="inl left b">
            <div class="center_wrapper">
                <div class="t center">
                    <div class="time">
                        {{ hour }}
                    </div>
                    <div class="ampm">
                        {{ ampm }}
                    </div>
                </div>
            </div>
        </div>
        <div class="inl mid b undline">
            
            <div class="center_wrapper">
                <div class="t center">
                    <div class="title">
                        {{ title }}
                    </div>
                    <div class="desc">
                        {{ desc }}
                    </div>
                    
            </div>
        </div>
        </div>
        <div class="inl right b undline">
            <!-- 为了实现垂直和水平同时居中出此下策，带个wrapper -->
            <div class="center_wrapper">
                <div class="type center">
                    {{ state }}
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>

const props = defineProps({
    title: String,
    desc: String,
    hour: String,
    ampm: String,
    state: String,
})

</script>

<style scoped>
.card {
    /* border: 1px solid red; */
    /* height: 100px; */
    margin-top: .5rem;
    border-radius: 10px;
    
    transition: background 0.7s;
}

.card:hover {
    background: #F0F0F0;
    
}

.card:active {
    background: #AAAAAA;
    
    transition: background 0s;
}

.inl {
    display: inline-table;
    
    padding-bottom: .5rem;
}

.left {
    width: 20%;
    /* height:4rem; */
    
    height: 3rem;
}

.mid {
    width: 60%;
    /* height:4rem; */
    
    height: 3rem;
}

.undline{
    border-color: #eeeeee;
    border-width: 0 0 .1rem 0;
    border-style: solid;
}

.time {
    font-size: .8em;
    font-weight: bold;
    margin: .2rem;
    text-align: center;
}

.ampm {
    /* background-color: red; */
    font-size: .6em;
    font-weight: bold;
    color:#909399;
    /* border: 1px solid #555; */
    background-color: #eeeeee;
    border-radius: .8em;
    width: 1.5rem;
    text-align: center;
    margin: .2rem;
    margin-left:auto;
    margin-right: auto;
}

.title {
    font-size: 1em;
    margin-bottom: .2rem;
    font-weight: bold;
}

.desc {
    color: grey;
    font-size: .7em;
}

.center_wrapper {
    display: table-cell;
    vertical-align: middle;
}

.center {
    margin-left: auto;
    margin-right: auto;
    
}

.type {
    font-size: 1em;
    margin: 3px;

    text-align: center;

    vertical-align: middle;
}

.t {
    /* border: 1px solid red; */
}

.right {
    height: 3rem;
}

.b{
    /* border: 1px solid blue; */
}

.content {
    border: 1px ridge #999;
    height: auto;
    min-height: 1000px;
    width: 1100px;
    margin-top: 40px;
    margin-right: auto;
    margin-bottom: 30px;
    margin-left: auto;
    float: left;
    position: relative;
    /* added */
    width: 100%;
    /* added */
}
</style>