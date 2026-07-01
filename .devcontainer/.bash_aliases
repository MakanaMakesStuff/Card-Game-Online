# .devcontainer/.bash_aliases

dj() {
    case "$1" in
        make) shift; poetry run python manage.py makemigrations "$@" ;;
        mig) shift; poetry run python manage.py migrate "$@" ;;
        run) shift; poetry run python manage.py runserver "$@" ;;
        super) shift; poetry run python manage.py createsuperuser "$@" ;;
        app) shift; poetry run python manage.py startapp "$@" ;;
        tw) shift; poetry run python manage.py tailwind "$@" ;;
        *) poetry run python manage.py "$@" ;;
    esac
}

alias ll="ls -la"