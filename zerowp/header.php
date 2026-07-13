<!DOCTYPE html>
<html <?php language_attributes(); ?>>

<head>
    <meta charset="<?php bloginfo('charset'); ?>">
    <meta http-equiv="Content-Type" content="text/html; charset=<?php bloginfo('charset'); ?>">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">

    <!-- Tailwind CSS v4 via CDN -->
    <script src="https://cdn.tailwindcss.com"></script>

    <?php
    // 获取 meta title
    $meta_title = wp_get_document_title();

    // 获取 meta description
    $description = '';
    if (is_singular()) {
        global $post;
        if (has_excerpt()) {
            $description = get_the_excerpt();
        } else {
            $description = wp_trim_words(strip_tags($post->post_content), 30, '');
        }
    } elseif (is_category() || is_tag()) {
        $description = term_description();
    } elseif (is_home() || is_front_page()) {
        $description = get_bloginfo('description');
    }
    ?>

    <meta name="title" content="<?php echo esc_attr($meta_title); ?>">
    <?php if ($description): ?>
        <meta name="description" content="<?php echo esc_attr($description); ?>">
    <?php endif; ?>

    <?php
    // 获取 canonical URL
    if (is_singular()) {
        $canonical_url = get_permalink();
    } elseif (is_home()) {
        $canonical_url = home_url('/');
    } elseif (is_404()) {
        $canonical_url = home_url('/404');
    } else {
        $term_link = get_term_link(get_queried_object());
        $canonical_url = !is_wp_error($term_link) ? $term_link : home_url('/');
    }
    ?>
    <link rel="canonical" href="<?php echo esc_url($canonical_url); ?>">

    <?php wp_head(); ?>
</head>

<body class="bg-white text-gray-900 antialiased">
    <?php wp_body_open(); ?>

    <div id="page" class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        <?php if (has_nav_menu('primary')): ?>
            <header class="py-6 border-b border-gray-200">
                <div class="flex items-center justify-between">
                    <a href="<?php echo esc_url(home_url('/')); ?>" class="text-xl font-bold tracking-tight hover:text-gray-600 transition-colors">
                        <?php bloginfo('name'); ?>
                    </a>

                    <nav class="flex items-center gap-6 text-sm">
                        <?php
                        wp_nav_menu(array(
                            'theme_location' => 'primary',
                            'container' => false,
                            'menu_class' => '',
                            'link_class' => 'text-gray-600 hover:text-gray-900 transition-colors',
                        ));
                        ?>
                    </nav>
                </div>
            </header>
        <?php endif; ?>

        <main class="py-8"><?php // 内容区域开始 
        ?>
