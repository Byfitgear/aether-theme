<?php
/**
 * 页面模板
 */
get_header();
?>

<article id="page-<?php the_ID(); ?>" <?php post_class('max-w-3xl mx-auto'); ?>>
    <div class="prose dark:prose-invert max-w-none">
        <?php the_content(); ?>
    </div>

    <?php if (comments_open() || get_comments_number()): ?>
        <div class="mt-12 pt-8 border-t border-gray-200 dark:border-gray-700">
            <?php comments_template(); ?>
        </div>
    <?php endif; ?>
</article>

<?php get_footer(); ?>
