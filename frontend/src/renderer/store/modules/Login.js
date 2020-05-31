const state = {
    loggedIn: false
}

const mutations = {
    LOGGED_IN(state) {
        state.loggedIn = true;
    },
    NOT_LOGGED_IN(state) {
        state.loggedIn = false;
    }
}

const actions = {
    loggedIn({ commit }) {
        commit('LOGGED_IN');
    },
    notLoggedIn({ commit }) {
        commit('NOT_LOGGED_IN')
    }
}

const getters = {
    loggedIn(state) {
        return state.loggedIn;
    }
}

export default {
    state,
    mutations,
    actions,
    getters
}
