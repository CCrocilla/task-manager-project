document.addEventListener('DOMContentLoaded', function () {
    // Sidenav Inizialization
    let sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav);

    // Datepicker Inizialization
    let datepicker = document.querySelectorAll('.datepicker');
    M.Datepicker.init(datepicker, {
        format: "dd mmmm, yyyy",
        i18n: {
            done: "Select"
        }
    });

    // Drop-Down Inizialization
    let selects = document.querySelectorAll('select');
    M.FormSelect.init(selects);

    // Collapsible Initialization
    let collapsible = document.querySelectorAll('.collapsible');
    M.Collapsible.init(collapsible);

});