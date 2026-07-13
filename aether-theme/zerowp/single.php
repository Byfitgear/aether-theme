<?php
/**
 * 单篇文章模板
 */
get_header();
?>

<article id="post-<?php the_ID(); ?>" <?php post_class('max-w-3xl mx-auto'); ?>>
    <header class="mb-8">
        <h1 class="text-3xl sm:text-4xl font-bold tracking-tight mb-4"><?php the_title(); ?></h1>
        <div class="flex items-center gap-2 text-sm text-gray-500">
            <time datetime="<?php echo get_the_date('c'); ?>">
                <?php echo get_the_date(); ?>
            </time>
            <span>·</span>
            <span><?php the_author(); ?></span>
            <?php if (has_category()): ?>
                <span>·</span>
                <span><?php the_category(', '); ?></span>
            <?php endif; ?>
        </div>
    </header>

    <?php if (has_post_thumbnail()): ?>
        <figure class="mb-8">
            <?php the_post_thumbnail('large', array('class' => 'rounded-lg w-full')); ?>
        </figure>
    <?php endif; ?>

    <div class="prose prose-gray max-w-none">
        <?php the_content(); ?>
    </div>

    <?php if (has_tag()): ?>
        <footer class="mt-12 pt-6 border-t border-gray-200">
            <div class="flex flex-wrap gap-2">
                <span class="text-sm text-gray-500"><?php _e('标签：', 'aether'); ?></span>
                <?php the_tags('', ', ', ''); ?>
            </div>
        </footer>
    <?php endif; ?>

    <?php if (comments_open() || get_comments_number()): ?>
        <div class="mt-12 pt-8 border-t border-gray-200">
            <?php comments_template(); ?>
        </div>
    <?php endif; ?>
</article>

<?php get_footer(); ?>
