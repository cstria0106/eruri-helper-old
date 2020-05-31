<template>
    <div id="course">
        <span id="name">{{data.name}}</span>
        <span id="professor">{{data.professor}}</span>
    </div>
</template>

<script>
export default {
    name: "course",
    props: ["data"]
};
</script>

<style lang="scss" scoped>
#course {
    border: 1px solid #ddd;
    border-radius: 5px;
    display: inline-block;
    padding: 10px;
    span {
        display: block;
        &#name {
            font-size: 1.2rem;
            margin-bottom: 10px;
        }
        &#professor {
            font-size: 0.9rem;
            color: #555;
        }
    }
}
</style>