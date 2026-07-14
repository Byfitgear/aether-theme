<?php
/**
 * 404 错误页面
 */
get_header();
?>

<div class="text-center py-24">
    <h1 class="text-8xl font-bold text-gray-200 dark:text-gray-700 mb-4">404</h1>
    <h2 class="text-2xl font-semibold text-gray-700 dark:text-gray-300 mb-2">
        <?php _e('页面未找到', 'aether'); ?>
    </h2>
    <p class="text-gray-500 dark:text-gray-400 mb-8">
        <?php _e('抱歉，您访问的页面不存在。', 'aether'); ?>
    </p>
    <a href="<?php echo esc_url(home_url('/')); ?>" class="inline-block px-6 py-2 bg-gray-900 dark:bg-gray-100 text-white dark:text-gray-900 rounded-lg hover:bg-gray-700 dark:hover:bg-gray-300 transition-colors text-sm font-medium">
        <?php _e('← 返回首页', 'aether'); ?>
    </a>
</div>

<?php get_footer(); ?>
