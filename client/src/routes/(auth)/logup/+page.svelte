<svelte:head>
    <title>Регистрация</title>
</svelte:head>

<script>
    import { toast } from "svelte-sonner";

    const uid = $props.id();
</script>

<form
    onsubmit={async (__event__) => {
        __event__.preventDefault();
        __event__.stopPropagation();
    }}
    class="p-4 flex flex-col gap-3 w-full min-w-[280px] max-w-[360px]"
>
    <h1 class="mb-4">Создание аккаунта</h1>
    <div class="field">
        <label for="{uid}-last_name">Фамилия</label>
        <input
            type="text"
            name="last_name"
            id="{uid}-last_name"
            autocomplete="off"
        />
    </div>
    <div class="field">
        <label for="{uid}-first_name">Имя</label>
        <input
            type="text"
            name="first_name"
            id="{uid}-first_name"
            autocomplete="off"
        />
    </div>
    <div class="field">
        <label for="{uid}-username">Имя пользователя</label>
        <input
            type="text"
            name="username"
            id="{uid}-username"
            autocomplete="off"
        />
    </div>
    <div class="field">
        <label for="{uid}-password">Пароль</label>
        <input
            type="password"
            name="password"
            id="{uid}-password"
            autocomplete="new-password webauthn"
        />
    </div>

    <p>Уже есть аккаунт? <a href="/login">Войти</a></p>

    <button type="submit">Зарегистрироваться</button>
</form>
