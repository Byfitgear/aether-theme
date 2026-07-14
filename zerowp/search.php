<?php
/**
 * 搜索模板
 */
get_header();
?>

<div class="max-w-3xl mx-auto">
    <header class="mb-8 pb-6 border-b border-gray-200 dark:border-gray-700">
        <h1 class="text-2xl font-bold">
            <?php printf(__('搜索结果：%s', 'aether'), '<span class="font-normal text-gray-500 dark:text-gray-400">' . esc_html(get_search_query()) . '</span>'); ?>
        </h1>
        <p class="text-sm text-gray-500 dark:text-gray-400 mt-1">
            <?php
            $count = $wp_query->found_posts;
            printf(_n('%d 条结果', '%d 条结果', $count, 'aether'), $count);
            ?>
        </p>
    </header>

    <div class="space-y-8">
        <?php if (have_posts()): ?>
            <?php while (have_posts()): the_post(); ?>
                <article class="pb-6 border-b border-gray-100 dark:border-gray-800">
                    <h2 class="text-lg font-semibold mb-1">
                        <a href="<?php the_permalink(); ?>" class="hover:text-gray-600 dark:hover:text-gray-300 transition-colors">
                            <?php the_title(); ?>
                        </a>
                    </h2>
                    <p class="text-sm text-gray-500 dark:text-gray-400 mb-2">
                        <time datetime="<?php echo get_the_date('c'); ?>"><?php echo esc_html(get_the_date()); ?></time>
                    </p>
                    <p class="text-gray-700 dark:text-gray-300 leading-relaxed">
                        <?php the_excerpt(); ?>
                    </p>
                </article>
            <?php endwhile; ?>

            <nav class="pt-6 border-t border-gray-200 dark:border-gray-700">
                <?php
                the_posts_pagination(array(
                    'prev_text' => __('← 上一页', 'aether'),
                    'next_text' => __('下一页 →', 'aether'),
                    'before_page_number' => '<span>' . __('页', 'aether') . ' </span>',
                ));
                ?>
            </nav>
        <?php else: ?>
            <div class="text-center py-12 text-gray-500 dark:text-gray-400">
                <p><?php _e('抱歉，未找到匹配的内容。', 'aether'); ?></p>
            </div>
        <?php endif; ?>
    </div>
</div>

<?php get_footer(); ?>
