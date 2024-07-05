const path = require('path');

module.exports = {
    entry: {
        base: [
            './modersite_js/base.ts',
            './modersite_js/base.scss',
        ],
        app: [
            './modersite_js/app.ts',
            './modersite_js/app.scss'
        ]
    },
    resolve: {
        extensions: ['.ts', '.js']
    },
    output: {
        filename: 'js/[name].js',
        path: path.resolve(__dirname, 'modersite/static'),
    },
    optimization: {
        minimize: false
    },

    module: {
        rules: [
            {
        test: /\.js$/,
        enforce: "pre",
        use: ["source-map-loader"],
      },
            {
                test: /\.ts$/,
                use: 'ts-loader',
                exclude: /node_modules/
            },
            {
                test: /\.scss$/,
                exclude: /node_modules/,
                type: 'asset/resource',
                generator: {filename: 'css/[name].css[query]'},
                use: [{loader: 'sass-loader', options: {sourceMap: true,}}]
            }
        ]
    },
    // Useful for debugging.
    devtool: 'source-map',
    performance: {hints: false}
}
/*
module.exports = {
    entry: {
        base: [
            './modersite_js/base.ts',
            './modersite_js/base.scss',
        ],
        app: [
            './modersite_js/app.ts',
            './modersite_js/app.scss'
        ]
    },
    devtool: 'source-map',
    output: {
        filename: 'js/[name].js',
        path: path.resolve(__dirname, 'modersite/static'),
    },
    module: {
        rules: [
            {
                test: /\.tsx?$/,
                use: 'ts-loader',
                exclude: /node_modules/,
                generator: {
                    filename: 'js/[name].js[query]',
                },
            },
            {
                test: /\.scss$/,
                exclude: /node_modules/,
                type: 'asset/resource',
                generator: {
                    filename: 'css/[name].css[query]',
                },
                use: [
                    {
                        loader: 'sass-loader', options: {
                            sourceMap: true,
                        },

                    }
                ]
            },
            {
                test: /\.(png|svg|jpg|jpeg|gif)$/i,
                type: 'asset/resource',
            },
            {
                test: /\.(woff|woff2|eot|ttf|otf)$/i,
                type: 'asset/resource',
            },
        ],
    },
    resolve: {
        extensions: ['.ts', '.js'],
    },

};
*/
