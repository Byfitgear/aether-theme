<?php
/**
 * 单篇文章模板
 */
get_header();
?>

<article id="post-<?php the_ID(); ?>" <?php post_class('max-w-3xl mx-auto'); ?>>
    <header class="mb-8">
        <?php if (has_category()): ?>
            <div class="flex gap-2 mb-3">
                <?php foreach (get_the_category() as $cat): ?>
                    <a href="<?php echo esc_url(get_category_link($cat->term_id)); ?>"
                       class="text-xs font-medium text-blue-600 dark:text-blue-400 hover:text-blue-800 dark:hover:text-blue-300 transition-colors">
                        <?php echo esc_html($cat->name); ?>
                    </a>
                <?php endforeach; ?>
            </div>
        <?php endif; ?>

        <h1 class="text-3xl sm:text-4xl font-bold tracking-tight mb-4"><?php the_title(); ?></h1>
        <div class="flex items-center gap-2 text-sm text-gray-500 dark:text-gray-400">
            <time datetime="<?php echo get_the_date('c'); ?>">
                <?php echo get_the_date(); ?>
            </time>
            <span>·</span>
            <span><?php the_author(); ?></span>
            <?php
            // 预估阅读时间（清理短代码和HTML标签）
            $content = strip_shortcodes(get_the_content());
            $content = strip_tags($content);
            $read_time = ceil(str_word_count($content) / 250);
            ?>
            <span>·</span>
            <span><?php printf(__('%d 分钟阅读', 'aether'), $read_time); ?></span>
        </div>
    </header>

    <?php if (has_post_thumbnail()): ?>
        <figure class="mb-8">
            <?php the_post_thumbnail('large', array('class' => 'rounded-lg w-full')); ?>
        </figure>
    <?php endif; ?>

    <div class="prose prose-gray dark:prose-invert max-w-none">
        <?php the_content(); ?>
    </div>

    <?php if (has_tag()): ?>
        <footer class="mt-12 pt-6 border-t border-gray-200 dark:border-gray-700">
            <div class="flex flex-wrap gap-2">
                <span class="text-sm text-gray-500 dark:text-gray-400"><?php _e('标签：', 'aether'); ?></span>
                <?php the_tags('', ', ', ''); ?>
            </div>
        </footer>
    <?php endif; ?>

    <!-- 文章导航 -->
    <nav class="mt-12 pt-6 border-t border-gray-200 dark:border-gray-700 grid grid-cols-2 gap-4">
        <?php
        $prev_post = get_previous_post();
        $next_post = get_next_post();
        ?>
        <?php if ($prev_post): ?>
            <a href="<?php echo esc_url(get_permalink($prev_post->ID)); ?>"
               class="group flex flex-col gap-1 p-3 rounded-lg hover:bg-gray-50 dark:hover:bg-gray-800 transition-colors">
                <span class="text-xs text-gray-400 dark:text-gray-500">← 上一篇</span>
                <span class="text-sm font-medium text-gray-700 dark:text-gray-300 group-hover:text-gray-900 dark:group-hover:text-gray-100 truncate">
                    <?php echo esc_html($prev_post->post_title); ?>
                </span>
            </a>
        <?php else: ?>
            <div></div>
        <?php endif; ?>

        <?php if ($next_post): ?>
            <a href="<?php echo esc_url(get_permalink($next_post->ID)); ?>"
               class="group flex flex-col gap-1 p-3 rounded-lg hover:bg-gray-50 dark:hover:bg-gray-800 transition-colors text-right">
                <span class="text-xs text-gray-400 dark:text-gray-500">下一篇 →</span>
                <span class="text-sm font-medium text-gray-700 dark:text-gray-300 group-hover:text-gray-900 dark:group-hover:text-gray-100 truncate">
                    <?php echo esc_html($next_post->post_title); ?>
                </span>
            </a>
        <?php else: ?>
            <div></div>
        <?php endif; ?>
    </nav>

    <?php if (comments_open() || get_comments_number()): ?>
        <div class="mt-12 pt-8 border-t border-gray-200 dark:border-gray-700">
            <?php comments_template(); ?>
        </div>
    <?php endif; ?>
</article>

<?php get_footer(); ?>
