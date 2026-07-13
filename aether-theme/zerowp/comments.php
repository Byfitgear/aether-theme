<?php
/**
 * 评论模板
 */
if (post_password_required()) {
    return;
}
?>

<section id="comments" class="mt-12">
    <?php if (have_comments()): ?>
        <h3 class="text-lg font-semibold mb-6">
            <?php
            $comment_count = get_comments_number();
            printf(_n('%s 条评论', '%s 条评论', $comment_count, 'aether'), number_format_i18n($comment_count));
            ?>
        </h3>

        <ol class="space-y-6">
            <?php wp_list_comments(array(
                'style'      => 'ol',
                'short_ping' => true,
                'callback'   => 'aether_comment_callback',
            )); ?>
        </ol>

        <?php
        the_comments_pagination(array(
            'prev_text' => '←',
            'next_text' => '→',
        ));
        ?>
    <?php endif; ?>

    <?php
    comment_form(array(
        'class_form'         => 'mt-8',
        'class_submit'       => 'px-4 py-2 bg-gray-900 text-white rounded-lg hover:bg-gray-700 transition-colors text-sm font-medium',
        'submit_button'      => '<button type="submit" class="%1$s">%2$s</button>',
    ));
    ?>
</section>
<?php

if (!function_exists('aether_comment_callback')):
    function aether_comment_callback($comment, $args, $depth) {
        $tag = 'li';
        ?>
        <<?php echo $tag; ?> id="comment-<?php comment_ID(); ?>" <?php comment_class(); ?>>
            <div class="flex gap-3">
                <div class="flex-shrink-0 w-8 h-8 rounded-full bg-gray-100 flex items-center justify-center text-sm font-medium text-gray-600">
                    <?php echo esc_html(get_comment_author()); ?>
                </div>
                <div class="flex-1">
                    <div class="flex items-center gap-2 text-sm mb-1">
                        <span class="font-medium"><?php comment_author(); ?></span>
                        <span class="text-gray-400"><?php comment_date('Y-m-d'); ?></span>
                        <?php comment_reply_link(array_merge($args, array('depth' => $depth, 'max_depth' => $args['max_depth']))); ?>
                    </div>
                    <div class="text-gray-700 leading-relaxed">
                        <?php comment_text(); ?>
                    </div>
                </div>
            </div>
        <?php
    }
endif;
