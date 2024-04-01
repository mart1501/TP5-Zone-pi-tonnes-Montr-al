'''
    This file contains the functions to call when
    a click is detected on the map, depending on the context
'''
import dash_html_components as html


def no_clicks(style):
    '''
        Deals with the case where the map was not clicked

        Args:
            style: The current display style for the panel
        Returns:
            title: The updated display title
            mode: The updated display title
            theme: The updated display theme
            style: The updated display style for the panel
    '''
    # TODO : Handle no clicks on the map
    return None, None, None, style


def map_base_clicked(title, mode, theme, style):
    '''
        Deals with the case where the map base is
        clicked (but not a marker)

        Args:
            title: The current display title
            mode: The current display title
            theme: The current display theme
            style: The current display style for the panel
        Returns:
            title: The updated display title
            mode: The updated display title
            theme: The updated display theme
            style: The updated display style for the panel
    '''
    # TODO : Handle clicks on the map base
    return title, mode, theme, style


def map_marker_clicked(figure, curve, point, title, mode, theme, style): # noqa : E501 pylint: disable=unused-argument too-many-arguments line-too-long
    '''
        Deals with the case where a marker is clicked

        Args:
            figure: The current figure
            curve: The index of the curve containing the clicked marker
            point: The index of the clicked marker
            title: The current display title
            mode: The current display title
            theme: The current display theme
            style: The current display style for the panel
        Returns:
            title: The updated display title
            mode: The updated display title
            theme: The updated display theme
            style: The updated display style for the panel
    '''
    # TODO : Handle clicks on the markers
    
    # Récupération de la couleur du marker
    color = figure['data'][curve]['marker']['color']
    
    # Récupération du titre - Type de l'intervention
    marker_title = figure['data'][curve]['customdata'][point][0]
    # Titre à afficher
    title = html.Div(marker_title, id='marker-title', style={'color': color, 'fontSize': '24px'})
    
    # Récupération du mode 
    marker_mode = figure['data'][curve]['customdata'][point][2]
    # Mode à afficher
    mode = html.Div(marker_mode, id='mode', style={'fontSize': '16px'})
    
    # Récupération des thèmes
    marker_theme = figure['data'][curve]['customdata'][point][3].split('\n')
    # Mode à afficher, sous forme d'une liste avec html.li et html.ul
    theme = html.Div([
        html.Div('Thématiques', style={'fontSize': '16px'}),
        html.Ul(id='my-list', children=[html.Li(t) for t in marker_theme])
    ]) 
    
    # Update du style pour le rendre visible
    style = {'visibility': 'visible',
             'border': '1px solid black',
             'padding': '10px'}
    
    return title, mode, theme, style
