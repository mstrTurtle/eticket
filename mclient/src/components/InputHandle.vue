<script setup>
import { ref, reactive, computed } from 'vue'

const t = ref(1)
const te = reactive({val:2})

const t_plus1 = computed(()=>{
  return t.value+1;
})


function onInput(e) {
  // t.value.v+=1
  t.value+=1
  te.val=t
  console.log(t)
  console.log(te)
  console.log(t_plus1)
}

function onChange(e){
  const k=e.key
  
  t.value=k
  if (k < 'a' || k > 'z') {
    e.preventDefault();
  }
  else{
    t.value = 1
  }
}

function onPrevent(e){
  // t.value = 10
}
</script>

<template>
  <button @click="onInput">
    <p>{{ t }}</p>
    <p>{{ te }}</p>
    <p>{{ t_plus1 }}</p>
  </button>
  <input type="text" @keypress="onChange" />
</template>