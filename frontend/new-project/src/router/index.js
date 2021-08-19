// import { processExpression } from '@vue/compiler-core'
// import Vue from 'vue'
import {createWebHistory, createRouter} from 'vue-router';
import Main from '@/views/Main.vue';
import Detail from '@/components/Detail';
import BoardList from '@/components/BoardList';
import Error from '@/components/Error';
import HelloWorld from '@/components/HelloWorld';


// const app=createApp(App);
// app.useAttrs(router);

// Vue.use(VueRouter)

// Vue.useAttrs(Router)

export const router = createRouter({
    history: createWebHistory(),

    routes :[
        {
            path:'/',
            name: 'Main',
            component : Main
        },
        {
            path:'/Detail/:contentId',
            name: 'Detail',
            component : Detail
        },
        {
            path:'/board2',
            name: 'Board2',
            component : BoardList
        },
        {
            path:'/board3',
            name: 'Board3',
            component : Error
        },
        {
            path:'/board4',
            name: 'Board4',
            component : HelloWorld
        },
    ]
})

// export default router;