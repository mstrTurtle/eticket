<script lang="ts" setup>
const username=localStorage.getItem("username")
</script>

<template>
    <span class="UserIcon">
            <el-avatar :size="64" :src="'https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png'" />
            </span>
      <h2>
      {{username}}
    </h2>
</template>

<style lang="scss" scoped>
</style>