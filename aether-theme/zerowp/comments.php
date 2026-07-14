<?php
/**
 * 评论模板
 */
if (!post_password_required()) : ?>
<section id="comments" class="mt-12">
    <?php if (have_comments()) : ?>
        <h3 class="text-lg font-semibold mb-6 text-gray-900 dark:text-gray-100">
            <?php
            $comment_count = get_comments_number();
            printf(_n('%s 条评论', '%s 条评论', $comment_count, 'aether'), number_format_i18n($comment_count));
            ?>
        </h3>

        <ol class="space-y-6 list-none">
            <?php
            wp_list_comments(array(
                'style'      => 'ol',
                'short_ping' => true,
                'callback'   => 'aether_comment_callback',
            ));
            ?>
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
        'class_form'      => 'mt-8',
        'class_submit'    => 'px-4 py-2 bg-gray-900 dark:bg-gray-100 text-white dark:text-gray-900 rounded-lg hover:bg-gray-700 dark:hover:bg-gray-300 transition-colors text-sm font-medium',
        'submit_button'   => '<button type="submit" class="%1$s">%2$s</button>',
    ));
    ?>
</section>
<?php endif;

if (!function_exists('aether_comment_callback')):
function aether_comment_callback($comment, $args, $depth) {
    $tag = 'li';
    ?>
    <<?php echo $tag; ?> id="comment-<?php comment_ID(); ?>" <?php comment_class(); ?>>
        <div class="flex gap-3">
            <div class="flex-shrink-0 w-8 h-8 rounded-full bg-gray-100 dark:bg-gray-800 flex items-center justify-center text-sm font-medium text-gray-600 dark:text-gray-400">
                <?php echo esc_html(get_comment_author()); ?>
            </div>
            <div class="flex-1">
                <div class="flex items-center gap-2 text-sm mb-1">
                    <span class="font-medium text-gray-900 dark:text-gray-100"><?php comment_author(); ?></span>
                    <span class="text-gray-400 dark:text-gray-500"><?php comment_date('Y-m-d'); ?></span>
                    <?php
                    if (comment_reply_link(array_merge($args, array(
                        'depth'     => $depth,
                        'max_depth' => $args['max_depth'],
                    )))) : ?>
                        <span class="text-blue-600 dark:text-blue-400 hover:text-blue-800 dark:hover:text-blue-300 cursor-pointer text-xs">回复</span>
                    <?php endif; ?>
                </div>
                <div class="text-gray-700 dark:text-gray-300 leading-relaxed">
                    <?php comment_text(); ?>
                </div>
            </div>
        </div>
    <?php
}
endif;
