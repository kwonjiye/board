<template>
<div>

<div class="container">
    <form>
        <input type="text" placeholder="검색어를 입력하세요" autofocus>
        <button type="reset" class="btn-reset">검색</button>
    </form>
</div>
    <a>{{search}}</a>
    <a>검색</a>
    <input type="text" 
    value=""  
    style="float:right; padding: 10px; border: 2px solid green;"
    @input="updateName">


    
</div>
</template>

<script>
export default {

props: {
    name: {
        type: String,
        required: true
        }
    },
    methods: {
        updateName(e) {
            console.log(e.target.value);
            this.$emit('update-name', e.target.value)
        }
    }
}
</script>
