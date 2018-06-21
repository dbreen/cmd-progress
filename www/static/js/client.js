$(function() {
    let $test_buttons = $('button.test-btn'),
        $progress_box = $('#progress-box'),
        $bar = $('.progress-bar');
    $test_buttons.click(function() {
        let command = $(this).data('command');
        $test_buttons.prop('disabled', true);
        $bar.text('0%').addClass('active');
        $progress_box.show();
        
        // Initiate the command, and we'll just get started right away without waiting
        $.get('/start-cmd/'+command);
        
        let interval = setInterval(function() {
            $.get('/get-progress/'+command, function(percent) {
                $bar.css('width', percent+'%');
                $bar.text(percent + '%');
                if(percent >= 100) {
                    clearInterval(interval);
                    $test_buttons.prop('disabled', false);
                    $bar.removeClass('active');
                }
            });
        }, 500);
    });
});
