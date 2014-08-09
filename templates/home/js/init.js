/*
	Helios by HTML5 UP
	html5up.net | @n33co
	Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
*/

(function($) {

	var settings = {
		
		// Header (homepage only)
			header: {
				fullScreen: true,
				fadeIn: true,
				fadeDelay: 500
			},

		// Carousels
			carousels: {
				speed: 4,
				fadeIn: true,
				fadeDelay: 250
			},
	
	};
	
	skel.init({
		reset: 'full',
		breakpoints: {
			'global':	{ range: '*', href: 'css/style.css', containers: 1400, grid: { gutters: 48 } },
			'wide':		{ range: '-1680', href: 'css/style-wide.css', containers: 1200 },
			'normal':	{ range: '-1280', href: 'css/style-normal.css', containers: '100%', grid: { gutters: 36 }, viewportWidth: 1140 },
			'narrow':	{ range: '-960', href: 'css/style-narrow.css', grid: { gutters: 32 }, viewportWidth: false },
			'narrower': { range: '-840', href: 'css/style-narrower.css', grid: { collapse: true } },
			'mobile':	{ range: '-640', href: 'css/style-mobile.css', grid: { gutters: 16 }, lockViewport: true }
		}
	}, {
		layers: {
			transformTest: function() { return skel.vars.isMobile; },
			layers: {
				navPanel: {
					hidden: true,
					breakpoints: 'mobile',
					position: 'top-left',
					side: 'top',
					width: '100%',
					height: 250,
					animation: 'pushY',
					clickToClose: true,
					swipeToClose: false,
					html: '<div data-action="navList" data-args="nav"></div>',
					orientation: 'vertical'
				},
				navButton: {
					breakpoints: 'mobile',
					position: 'top-center',
					side: 'top',
					width: 100,
					height: 50,
					html: '<div class="toggle" data-action="toggleLayer" data-args="navPanel"></div>'
				}
			}
		}
	});

	$(function() {

		var	$window = $(window),
			$body = $('body'),
			$header =  $('#header');
			
		// Disable animations/transitions until the page has loaded.
			$body.addClass('is-loading');
			
			$window.on('load', function() {
				$body.removeClass('is-loading');
			});
			
		// CSS polyfills (IE<9).
			if (skel.vars.IEVersion < 9)
				$(':last-child').addClass('last-child');

		// Forms (IE<10).
			var $form = $('form');
			if ($form.length > 0) {
				
				$form.find('.form-button-submit')
					.on('click', function() {
						$(this).parents('form').submit();
						return false;
					});
		
				if (skel.vars.IEVersion < 10) {
					$.fn.n33_formerize=function(){var _fakes=new Array(),_form = $(this);_form.find('input[type=text],textarea').each(function() { var e = $(this); if (e.val() == '' || e.val() == e.attr('placeholder')) { e.addClass('formerize-placeholder'); e.val(e.attr('placeholder')); } }).blur(function() { var e = $(this); if (e.attr('name').match(/_fakeformerizefield$/)) return; if (e.val() == '') { e.addClass('formerize-placeholder'); e.val(e.attr('placeholder')); } }).focus(function() { var e = $(this); if (e.attr('name').match(/_fakeformerizefield$/)) return; if (e.val() == e.attr('placeholder')) { e.removeClass('formerize-placeholder'); e.val(''); } }); _form.find('input[type=password]').each(function() { var e = $(this); var x = $($('<div>').append(e.clone()).remove().html().replace(/type="password"/i, 'type="text"').replace(/type=password/i, 'type=text')); if (e.attr('id') != '') x.attr('id', e.attr('id') + '_fakeformerizefield'); if (e.attr('name') != '') x.attr('name', e.attr('name') + '_fakeformerizefield'); x.addClass('formerize-placeholder').val(x.attr('placeholder')).insertAfter(e); if (e.val() == '') e.hide(); else x.hide(); e.blur(function(event) { event.preventDefault(); var e = $(this); var x = e.parent().find('input[name=' + e.attr('name') + '_fakeformerizefield]'); if (e.val() == '') { e.hide(); x.show(); } }); x.focus(function(event) { event.preventDefault(); var x = $(this); var e = x.parent().find('input[name=' + x.attr('name').replace('_fakeformerizefield', '') + ']'); x.hide(); e.show().focus(); }); x.keypress(function(event) { event.preventDefault(); x.val(''); }); });  _form.submit(function() { $(this).find('input[type=text],input[type=password],textarea').each(function(event) { var e = $(this); if (e.attr('name').match(/_fakeformerizefield$/)) e.attr('name', ''); if (e.val() == e.attr('placeholder')) { e.removeClass('formerize-placeholder'); e.val(''); } }); }).bind("reset", function(event) { event.preventDefault(); $(this).find('select').val($('option:first').val()); $(this).find('input,textarea').each(function() { var e = $(this); var x; e.removeClass('formerize-placeholder'); switch (this.type) { case 'submit': case 'reset': break; case 'password': e.val(e.attr('defaultValue')); x = e.parent().find('input[name=' + e.attr('name') + '_fakeformerizefield]'); if (e.val() == '') { e.hide(); x.show(); } else { e.show(); x.hide(); } break; case 'checkbox': case 'radio': e.attr('checked', e.attr('defaultValue')); break; case 'text': case 'textarea': e.val(e.attr('defaultValue')); if (e.val() == '') { e.addClass('formerize-placeholder'); e.val(e.attr('placeholder')); } break; default: e.val(e.attr('defaultValue')); break; } }); window.setTimeout(function() { for (x in _fakes) _fakes[x].trigger('formerize_sync'); }, 10); }); return _form; };
					$form.n33_formerize();
				}

			}

		// Dropdowns.
			$('#nav > ul').dropotron({ 
				mode: 'fade',
				speed: 350,
				noOpenerFade: true,
				alignment: 'center'
			});

		// Scrolly links.
			$('.scrolly').scrolly();			

		// Carousels.
			$('.carousel').each(function() {
				
				var	$t = $(this),
					$forward = $('<span class="forward"></span>'),
					$backward = $('<span class="backward"></span>'),
					$reel = $t.children('.reel'),
					$items = $reel.children('article');
				
				var	pos = 0,
					leftLimit,
					rightLimit,
					itemWidth,
					reelWidth,
					timerId;

				// Items.
					if (settings.carousels.fadeIn) {
						
						$items.addClass('loading');

						$t.onVisible(function() {
							var	timerId,
								limit = $items.length - Math.ceil($window.width() / itemWidth);
							
							timerId = window.setInterval(function() {
								var x = $items.filter('.loading'), xf = x.first();
								
								if (x.length <= limit) {
									
									window.clearInterval(timerId);
									$items.removeClass('loading');
									return;
								
								}
								
								if (skel.vars.IEVersion < 10) {
									
									xf.fadeTo(750, 1.0);
									window.setTimeout(function() {
										xf.removeClass('loading');
									}, 50);
								
								}
								else
									xf.removeClass('loading');
								
							}, settings.carousels.fadeDelay);
						}, 50);
					}
				
				// Main.
					$t._update = function() {
						pos = 0;
						rightLimit = (-1 * reelWidth) + $window.width();
						leftLimit = 0;
						$t._updatePos();
					};
				
					if (skel.vars.IEVersion < 9)
						$t._updatePos = function() { $reel.css('left', pos); };
					else
						$t._updatePos = function() { $reel.css('transform', 'translate(' + pos + 'px, 0)'); };
					
				// Forward.
					$forward
						.appendTo($t)
						.hide()
						.mouseenter(function(e) {
							timerId = window.setInterval(function() {
								pos -= settings.carousels.speed;

								if (pos <= rightLimit)
								{
									window.clearInterval(timerId);
									pos = rightLimit;
								}
								
								$t._updatePos();
							}, 10);
						})
						.mouseleave(function(e) {
							window.clearInterval(timerId);
						});
				
				// Backward.
					$backward
						.appendTo($t)
						.hide()
						.mouseenter(function(e) {
							timerId = window.setInterval(function() {
								pos += settings.carousels.speed;

								if (pos >= leftLimit) {
									
									window.clearInterval(timerId);
									pos = leftLimit;
								
								}
								
								$t._updatePos();
							}, 10);
						})
						.mouseleave(function(e) {
							window.clearInterval(timerId);
						});
						
				// Init.
					$window.load(function() {

						reelWidth = $reel[0].scrollWidth;

						skel.onStateChange(function() {
				
							if (skel.vars.isTouch) {
								
								$reel
									.css('overflow-y', 'hidden')
									.css('overflow-x', 'scroll')
									.scrollLeft(0);
								$forward.hide();
								$backward.hide();
							
							}
							else {
								
								$reel
									.css('overflow', 'visible')
									.scrollLeft(0);
								$forward.show();
								$backward.show();
							
							}

							$t._update();
						});

						$window.resize(function() {
							reelWidth = $reel[0].scrollWidth;
							$t._update();
						}).trigger('resize');

					});
				
			});
		
		// Header.
			if ($body.hasClass('homepage')) {
				
				if (settings.header.fullScreen) {
					
					$window.bind('resize.helios', function() {
						window.setTimeout(function() {
							var s = $header.children('.inner');
							var sh = s.outerHeight(), hh = $window.height(), h = Math.ceil((hh - sh) / 2) + 1;

							$header
								.css('padding-top', h)
								.css('padding-bottom', h);
						}, 0);
					}).trigger('resize');
				
				}

				if (settings.header.fadeIn) {

					$.n33_preloadImage = function(url, onload) { var $img = $('<img />'), _IEVersion = (navigator.userAgent.match(/MSIE ([0-9]+)\./) ? parseInt(RegExp.$1) : 99); $img.attr('src', url); if ($img.get(0).complete || _IEVersion < 9) (onload)(); else $img.load(onload); };
					
					$('<div class="overlay" />').appendTo($header);
					
					$window
						.load(function() {
							var imageURL = $header.css('background-image').replace(/"/g,"").replace(/url\(|\)$/ig, "");

							$.n33_preloadImage(imageURL, function() {
								
								if (skel.vars.IEVersion < 10)
									$header.children('.overlay').fadeOut(2000);
								else
									window.setTimeout(function() {
										$header.addClass('ready');
									}, settings.header.fadeDelay);
							
							});
						});
				
				}

			}

	});

})(jQuery);