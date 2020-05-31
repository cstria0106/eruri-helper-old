const state = {
    courses: []
}

const mutations = {
    ADD_COURSE(state, course) {
        state.courses.push(course);
    },
    ADD_COURSES(state, courses) {
        state.courses = state.courses.concat(courses);
    },
    UPDATE_COURSE(state, course) {
        for (let i = 0; i < state.courses.length; i++) {
            if (state.courses[i].id == course.id) {
                state.courses[i] = course;
            }
        }
    },
    CLEAR_COURSES(state) {
        state.courses = [];
    }
}

const actions = {
    addCourse({ commit }, course) {
        commit('ADD_COURSE', course);
    },
    addCourses({ commit }, courses) {
        commit('ADD_COURSES', courses);
    },
    updateCourse({ commit }, course) {
        commit('UPDATE_COURSE', course);
    },
    clearCourses({ commit }) {
        commit('CLEAR_COURSES');
    }
}

const getters = {
    courses: (state) => {
        return state.courses;
    }
}

export default {
    state,
    mutations,
    actions,
    getters
}
