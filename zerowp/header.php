<!DOCTYPE html>
<html <?php language_attributes(); ?>>

<head>
    <meta charset="<?php bloginfo('charset'); ?>">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">

    <!-- Tailwind CSS v4 — local build (preferred) or CDN fallback -->
    <?php
    $css_file = get_template_directory() . '/assets/css/output.css';
    if (file_exists($css_file)) {
        $css_version = filemtime($css_file);
        echo '<link rel="stylesheet" href="' . esc_url(get_template_directory_uri() . '/assets/css/output.css') . '?v=' . esc_attr($css_version) . '">';
    } else {
        echo '<script src="https://cdn.tailwindcss.com"></script>';
    }
    ?>

    <?php
    // Meta title
    $meta_title = wp_get_document_title();

    // Meta description
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

    // Canonical URL
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

    // OG tags
    $og_title = $meta_title;
    $og_description = $description ?: get_bloginfo('name') . ' — ' . get_bloginfo('description');
    $og_image = '';
    if (is_singular() && has_post_thumbnail()) {
        $thumbnail = wp_get_attachment_image_src(get_post_thumbnail_id(), 'large');
        $og_image = $thumbnail[0];
    } elseif (is_home() || is_front_page()) {
        $custom_logo_id = get_theme_mod('custom_logo');
        if ($custom_logo_id) {
            $logo = wp_get_attachment_image_src($custom_logo_id, 'medium');
            if ($logo) $og_image = $logo[0];
        }
    }
    ?>

    <meta name="title" content="<?php echo esc_attr($meta_title); ?>">
    <?php if ($description): ?>
        <meta name="description" content="<?php echo esc_attr($description); ?>">
    <?php endif; ?>
    <link rel="canonical" href="<?php echo esc_url($canonical_url); ?>">

    <!-- Open Graph -->
    <meta property="og:type" content="<?php echo is_singular() ? 'article' : 'website'; ?>">
    <meta property="og:title" content="<?php echo esc_attr($og_title); ?>">
    <meta property="og:description" content="<?php echo esc_attr($og_description); ?>">
    <?php if ($og_image): ?>
        <meta property="og:image" content="<?php echo esc_url($og_image); ?>">
    <?php endif; ?>
    <meta property="og:url" content="<?php echo esc_url($canonical_url); ?>">
    <meta property="og:site_name" content="<?php echo esc_attr(get_bloginfo('name')); ?>">

    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="<?php echo esc_attr($og_title); ?>">
    <meta name="twitter:description" content="<?php echo esc_attr($og_description); ?>">
    <?php if ($og_image): ?>
        <meta name="twitter:image" content="<?php echo esc_url($og_image); ?>">
    <?php endif; ?>

    <?php wp_head(); ?>
</head>

<body <?php body_class("bg-white text-gray-900 antialiased"); ?>>
    <?php wp_body_open(); ?>

    <div id="page" class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        <?php if (has_nav_menu('primary')): ?>
            <header class="py-6 border-b border-gray-200 dark:border-gray-700">
                <div class="flex items-center justify-between">
                    <?php aether_site_logo(); ?>

                    <nav class="flex items-center gap-4 text-sm">
                        <?php
                        wp_nav_menu(array(
                            'theme_location' => 'primary',
                            'container' => false,
                            'menu_class' => '',
                            'link_class'   => 'text-gray-600 hover:text-gray-900 dark:text-gray-400 dark:hover:text-gray-100 transition-colors',
                        ));
                        ?>

                        <!-- Dark Mode Toggle -->
                        <button id="aether-dark-toggle" type="button" aria-label="切换暗色模式"
                                class="ml-2 p-1.5 rounded-lg text-gray-500 hover:bg-gray-100 dark:hover:bg-gray-800 dark:text-gray-400 transition-colors">
                            <svg id="icon-sun" class="w-5 h-5 hidden" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"/>
                            </svg>
                            <svg id="icon-moon" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"/>
                            </svg>
                        </button>
                    </nav>
                </div>
            </header>
        <?php endif; ?>

        <main class="py-8">
