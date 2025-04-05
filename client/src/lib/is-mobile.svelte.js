import { MediaQuery } from 'svelte/reactivity';

export default class IsMobile extends MediaQuery {
    constructor() {
        super(`max-width: 980px`);
    }
}
