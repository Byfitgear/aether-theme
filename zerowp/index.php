<?php
/**
 * 主模板文件
 */
get_header();
?>

<div class="space-y-12">
    <?php if (have_posts()): ?>
        <?php while (have_posts()): the_post(); ?>
            <article id="post-<?php the_ID(); ?>" <?php post_class('border-b border-gray-100 dark:border-gray-800 pb-12 last:border-0'); ?>>
                <header>
                    <h2 class="text-2xl font-bold mb-2">
                        <a href="<?php the_permalink(); ?>" class="hover:text-gray-600 dark:hover:text-gray-300 transition-colors">
                            <?php the_title(); ?>
                        </a>
                    </h2>
                    <time datetime="<?php echo get_the_date('c'); ?>" class="text-sm text-gray-500 dark:text-gray-400">
                        <?php echo esc_html(get_the_date()); ?>
                    </time>
                </header>

                <div class="mt-4 text-gray-700 dark:text-gray-300 leading-relaxed">
                    <?php the_excerpt(); ?>
                </div>

                <footer class="mt-4">
                    <a href="<?php the_permalink(); ?>" class="text-blue-600 hover:text-blue-800 dark:text-blue-400 dark:hover:text-blue-300 transition-colors text-sm font-medium">
                        <?php _e('继续阅读', 'aether'); ?> →
                    </a>
                </footer>
            </article>
        <?php endwhile; ?>

        <nav class="flex justify-between items-center pt-8 border-t border-gray-200 dark:border-gray-700">
            <?php
            the_posts_pagination(array(
                'prev_text' => __('← 上一页', 'aether'),
                'next_text' => __('下一页 →', 'aether'),
                'before_page_number' => '<span>' . __('页', 'aether') . ' </span>',
            ));
            ?>
        </nav>
    <?php else: ?>
        <div class="text-center py-12">
            <h2 class="text-xl font-semibold text-gray-500 dark:text-gray-400"><?php _e('暂无内容', 'aether'); ?></h2>
            <p class="text-gray-400 dark:text-gray-500 mt-2"><?php _e('抱歉，未找到任何内容。', 'aether'); ?></p>
        </div>
    <?php endif; ?>
</div>

<?php get_footer(); ?>
